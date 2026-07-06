# PII Schema Scout

![PII Schema Scout cover](assets/readme-cover.svg)

> Find privacy-sensitive fields in schemas, exports, and data dictionaries

![stack](https://img.shields.io/badge/stack-Python-16a34a?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-dc2626?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-7c3aed?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-0891b2?style=flat-square)

## At a glance

| Area | Detail |
| --- | --- |
| Focus | schema hygiene |
| Command | `pii-schema-scout` |
| Formats | text, JSON, JSONL, CSV |
| Output | Markdown table or JSON |

## What it checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `government-id-field` | high | government identifier field detected |
| `contact-pii-field` | medium | direct contact or identity field detected |
| `location-field` | low | location-like field detected |

## Try it locally

```bash
python -m pip install -e ".[dev]"
pii-schema-scout examples/sample.txt
pii-schema-scout examples/sample.txt --json --fail-on medium
```

## Notes from the code

`rules.py` keeps the project policy explicit, while `core.py` handles parsing and report rendering. The CLI stays thin on purpose so the checks are easy to test.

## Verify

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m pii_schema_scout --help
```
