"""Configuration specific to Graphenda Build.

Extends SharedConfig with Build-specific settings.

Public environment-variable contract (see ``.env.example``):
    NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, NEO4J_DATABASE       (via SharedConfig)
    ANTHROPIC_API_KEY, ANTHROPIC_MODEL
    GRAPHENDA_REGISTRY_PATH, GRAPHENDA_ONTOLOGIES_PATH
    LOG_LEVEL, LOG_FORMAT
"""
import os
from dataclasses import dataclass
from graphenda_shared.config import SharedConfig, Neo4jConfig


@dataclass
class BuildConfig(SharedConfig):
    """Configuration for the Graph Construction Engine."""
    ontologies_dir: str = os.getenv("GRAPHENDA_ONTOLOGIES_PATH", "./ontologies")
    registry_dir: str = os.getenv("GRAPHENDA_REGISTRY_PATH", "../graphenda-registry")
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")
    extraction_model: str = os.getenv("ANTHROPIC_MODEL", "claude-opus-4-7")
    chunk_size: int = int(os.getenv("CHUNK_SIZE", "1000"))
    chunk_overlap: int = int(os.getenv("CHUNK_OVERLAP", "200"))
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    log_format: str = os.getenv("LOG_FORMAT", "text")
