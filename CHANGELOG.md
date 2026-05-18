# Changelog

All notable changes to `graphenda-build` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] — 2026-05-18
### Added
- Initial extraction from monorepo (formerly `Graphenda/build/`).
- Package `graphenda_build` with submodules: ingestion, ontology, graph, hierarchy, community, quality, registry, core.
- 5 ontologies migrated: panelbox, ai_governance, model_intelligence, model_validation, bias_intelligence.
- CLI scripts: ingest, build_hierarchy, create_instance.
- Docker stack minima (Neo4j + Build job).
- Dependency pin to `graphenda-shared v0.1.0`.
