"""Graph Registry publisher — publishes graphs from Build to Registry.

After building a graph, use the publisher to register it in the catalog
so the SaaS can discover and serve it.

The target registry directory is resolved with this precedence:
    1. Explicit ``registry_dir`` argument to :class:`RegistryPublisher`.
    2. Environment variable ``GRAPHENDA_REGISTRY_PATH``.
    3. Default: ``<repo-root>/../graphenda-registry`` (sibling of graphenda-build).
"""
import difflib
import logging
import os
import yaml
from datetime import datetime
from pathlib import Path
from typing import Optional, Union

from graphenda_shared.registry.models import GraphRegistryEntry, GraphStatus, GraphMetrics

logger = logging.getLogger(__name__)

ENV_REGISTRY_PATH = "GRAPHENDA_REGISTRY_PATH"


def _default_registry_dir() -> Path:
    """Resolve the default registry directory: sibling ``graphenda-registry/``."""
    return Path(__file__).resolve().parents[3] / "graphenda-registry"


def resolve_registry_dir(registry_dir: Optional[Union[str, Path]] = None) -> Path:
    """Resolve the effective registry directory.

    Precedence: explicit argument > ``GRAPHENDA_REGISTRY_PATH`` env > default sibling.
    """
    if registry_dir is not None:
        return Path(registry_dir)
    env_value = os.environ.get(ENV_REGISTRY_PATH)
    if env_value:
        return Path(env_value)
    return _default_registry_dir()


class RegistryYAMLConflict(RuntimeError):
    """Raised when an existing YAML differs from new content and ``force`` is False."""

    def __init__(self, path: Path, diff: str):
        super().__init__(
            f"Registry entry already exists with different content: {path}\n"
            f"Pass force=True to overwrite.\nDiff:\n{diff}"
        )
        self.path = path
        self.diff = diff


class RegistryPublisher:
    """Publishes graph entries to the registry."""

    def __init__(self, registry_dir: Optional[Union[str, Path]] = None):
        self.registry_dir = resolve_registry_dir(registry_dir).resolve()
        self.registry_dir.mkdir(parents=True, exist_ok=True)
        logger.info("RegistryPublisher writing to: %s", self.registry_dir)

    def publish(self, entry: GraphRegistryEntry, force: bool = False) -> Path:
        """Write a registry entry to YAML file.

        Args:
            entry: The graph registry entry to publish.
            force: When False (default), refuse to overwrite an existing YAML whose
                content differs from the new one; raises :class:`RegistryYAMLConflict`
                with a unified diff. When True, overwrite unconditionally.

        Returns:
            Path to the created/updated YAML file.
        """
        path = self.registry_dir / f"{entry.slug}.yaml"

        data = {
            "slug": entry.slug,
            "name": entry.name,
            "description": entry.description,
            "version": entry.version,
            "status": entry.status.value,
            "neo4j_database": entry.neo4j_database,
            "ontology": entry.ontology,
            "hierarchy_levels": entry.hierarchy_levels,
            "metrics": {
                "nodes": entry.metrics.nodes,
                "edges": entry.metrics.edges,
                "communities": entry.metrics.communities,
                "avg_confidence": entry.metrics.avg_confidence,
                "coverage": entry.metrics.coverage,
                "last_updated": datetime.now().strftime("%Y-%m-%d"),
            },
            "retrievers": entry.retrievers,
            "domain": {
                "color": entry.domain.color,
                "icon": entry.domain.icon,
                "category": entry.domain.category,
                "tags": entry.domain.tags,
            },
            "thresholds": {
                "min_confidence": entry.thresholds.min_confidence,
                "min_nodes_for_active": entry.thresholds.min_nodes_for_active,
                "curation_review_days": entry.thresholds.curation_review_days,
            },
        }

        new_yaml = yaml.dump(data, default_flow_style=False, sort_keys=False)

        if path.exists() and not force:
            existing_yaml = path.read_text()
            if existing_yaml != new_yaml:
                diff = "".join(
                    difflib.unified_diff(
                        existing_yaml.splitlines(keepends=True),
                        new_yaml.splitlines(keepends=True),
                        fromfile=f"{path.name} (existing)",
                        tofile=f"{path.name} (new)",
                    )
                )
                raise RegistryYAMLConflict(path, diff)

        path.write_text(new_yaml)
        return path

    def update_metrics(self, slug: str, metrics: GraphMetrics) -> None:
        """Update only the metrics section of a registry entry."""
        from graphenda_shared.registry.reader import RegistryReader

        reader = RegistryReader(self.registry_dir)
        entry = reader.load(slug)
        entry.metrics = metrics
        self.publish(entry, force=True)

    def set_status(self, slug: str, status: GraphStatus) -> None:
        """Change the status of a graph in the registry."""
        from graphenda_shared.registry.reader import RegistryReader

        reader = RegistryReader(self.registry_dir)
        entry = reader.load(slug)
        entry.status = status
        if status == GraphStatus.ACTIVE:
            entry.published_at = datetime.now()
        self.publish(entry, force=True)
