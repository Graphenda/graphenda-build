"""Community summarization using Claude API.

Generates concise thematic summaries for graph communities detected
by the Leiden algorithm. Summaries are cached to disk to avoid
redundant API calls.
"""

import hashlib
import json
import logging
from pathlib import Path
from typing import Any

from graphenda_build.llm import LLMMessage, LLMProvider
from graphenda_build.ontology.manager import OntologySchema
from graphenda_shared.graph.connection import Neo4jConnection

logger = logging.getLogger(__name__)

# Domain-agnostic prompt template — the ontology description is injected at runtime
SUMMARY_PROMPT_TEMPLATE = """You are an expert analyst for a knowledge graph.

Domain: {domain_description}

Below is a community (cluster) of related entities from the knowledge graph.
Each entity has a type and may have a description.

Community members:
{members_text}

Relationships between members:
{relationships_text}

Write a concise summary (3-5 sentences) of this community. Include:
1. The main theme or domain of this community
2. The key entities or concepts it contains
3. How the members relate to each other
4. Typical use cases or when a user would need this information

Be specific about the domain concepts."""


class CommunitySummarizer:
    """Generates human-readable summaries for graph communities using Claude."""

    def __init__(
        self,
        connection: Neo4jConnection,
        llm: LLMProvider,
        ontology: OntologySchema,
        model: str | None = None,
        cache_dir: str | Path | None = None,
    ) -> None:
        self._conn = connection
        self._llm = llm
        self._ontology = ontology
        self._model = model
        self._cache_dir = Path(cache_dir) if cache_dir else Path("data/community_cache")
        self._cache_dir.mkdir(parents=True, exist_ok=True)

    def summarize_all(self) -> list[dict[str, Any]]:
        """Summarize all communities found in Neo4j."""
        communities = self._get_all_communities()
        if not communities:
            logger.warning("No communities found in Neo4j")
            return []

        cached = self._load_cached_summaries()
        results = []

        for cid, members in communities.items():
            cache_key = self._compute_cache_key(cid, members)
            if cache_key in cached:
                summary = cached[cache_key]
            else:
                logger.info("Generating summary for community %d (%d members)", cid, len(members))
                summary = self.summarize_community(cid, members)
                self._save_to_cache(cache_key, summary)

            self._store_summary(cid, summary, [m["name"] for m in members])
            results.append({
                "community_id": cid,
                "summary": summary,
                "members": [m["name"] for m in members],
                "member_count": len(members),
            })

        return results

    def summarize_community(self, community_id: int, members: list[dict[str, Any]]) -> str:
        """Generate a summary for a single community via the LLM provider."""
        prompt = self._build_summary_prompt(members)
        try:
            text = self._llm.complete(
                messages=[LLMMessage(role="user", content=prompt)],
                model=self._model,
                max_tokens=300,
                temperature=0.3,
            )
            return text.strip()
        except Exception as e:
            logger.error("Failed to summarize community %d: %s", community_id, e)
            names = [m.get("name", "unknown") for m in members]
            return f"This community contains {len(members)} related entities: {', '.join(names[:10])}."

    def _build_summary_prompt(self, members: list[dict[str, Any]]) -> str:
        members_lines = []
        for m in members:
            name = m.get("name", "unknown")
            labels = m.get("labels", [])
            desc = m.get("description", "")
            label_str = ", ".join(labels) if labels else "Entity"
            line = f"- {name} ({label_str})"
            if desc:
                line += f": {desc[:200]}"
            members_lines.append(line)

        member_names = [m.get("name", "") for m in members]
        relationships_text = self._get_relationships_text(member_names)

        return SUMMARY_PROMPT_TEMPLATE.format(
            domain_description=self._ontology.description,
            members_text="\n".join(members_lines),
            relationships_text=relationships_text or "No explicit relationships found.",
        )

    def _get_relationships_text(self, member_names: list[str]) -> str:
        records = self._conn.run(
            "MATCH (a)-[r]->(b) WHERE a.name IN $names AND b.name IN $names "
            "RETURN a.name AS source, type(r) AS rel, b.name AS target LIMIT 50",
            {"names": member_names},
        )
        return "\n".join(f"- {r['source']} --[{r['rel']}]--> {r['target']}" for r in records)

    def _store_summary(self, community_id: int, summary: str, member_names: list[str]) -> None:
        community_name = f"Community_{community_id}"
        self._conn.run("MATCH (c:Community {community_id: $id}) DETACH DELETE c", {"id": community_id})
        self._conn.run(
            "CREATE (c:Community {community_id: $id, name: $name, summary: $summary, member_count: $count})",
            {"id": community_id, "name": community_name, "summary": summary, "count": len(member_names)},
        )
        for name in member_names:
            self._conn.run(
                "MATCH (n) WHERE n.name = $name AND n.community_id = $cid "
                "MATCH (c:Community {community_id: $cid}) "
                "MERGE (n)-[:MEMBER_OF]->(c)",
                {"name": name, "cid": community_id},
            )

    def _get_all_communities(self) -> dict[int, list[dict[str, Any]]]:
        records = self._conn.run(
            "MATCH (n) WHERE n.community_id IS NOT NULL "
            "RETURN n.community_id AS cid, n.name AS name, labels(n) AS labels, "
            "n.description AS description ORDER BY n.community_id"
        )
        communities: dict[int, list[dict[str, Any]]] = {}
        for rec in records:
            communities.setdefault(rec["cid"], []).append({
                "name": rec["name"], "labels": rec["labels"], "description": rec["description"],
            })
        return communities

    def _compute_cache_key(self, community_id: int, members: list[dict[str, Any]]) -> str:
        names = sorted(m.get("name", "") for m in members)
        return hashlib.sha256(f"{community_id}:{','.join(names)}".encode()).hexdigest()[:16]

    def _load_cached_summaries(self) -> dict[str, str]:
        cache_file = self._cache_dir / "summaries.json"
        if not cache_file.exists():
            return {}
        try:
            return json.loads(cache_file.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return {}

    def _save_to_cache(self, cache_key: str, summary: str) -> None:
        cache_file = self._cache_dir / "summaries.json"
        cached = self._load_cached_summaries()
        cached[cache_key] = summary
        try:
            cache_file.write_text(json.dumps(cached, ensure_ascii=False, indent=2), encoding="utf-8")
        except OSError as e:
            logger.warning("Failed to save summary cache: %s", e)
