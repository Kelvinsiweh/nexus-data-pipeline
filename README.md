# Nexus Data Pipeline

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An extensible, production-ready ETL (Extract, Transform, Load) and analytical data processing pipeline developed in Python.

## Features
- **Multi-source Extraction**: CSV, JSON Lines, and in-memory streams
- **Schema Validation**: Built with modern Pydantic v2 data models
- **Transformations**: Normalization, deduplication, anomaly filtering, metric aggregation
- **Rich Reporting**: Formatted terminal output and Markdown reports
- **Intuitive CLI**: Powered by Click

## Architecture
```
[ Raw Data Sources ]
        │
        ▼
[ Extraction Engine ] ──► [ Schema Validation (Pydantic) ]
        │
        ▼
[ Transformation Pipeline ] ──► [ Aggregation & Metrics ]
        │
        ▼
[ Loaders & Reporters ] ──► [ Terminal UI / Markdown Reports ]
```

## Installation
```bash
pip install -e .
```

## Quick Start
```bash
nexus process --sample
```
