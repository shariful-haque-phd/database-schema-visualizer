# Architecture — Database Schema Visualizer

```mermaid
flowchart LR
    A["schema.sql"] --> B["schema_to_mermaid.py"]
    B --> C["schema.html, schema.mmd"]
```

## Inputs

- `sample/schema.sql`

## Source files

- `src/schema_to_mermaid.py`

## Output

- `results/artifacts/schema.html`
- `results/artifacts/schema.mmd`

This representation is intended for source navigation. It does not imply a production deployment or undisclosed components. The editable diagram is available as [`architecture.mmd`](architecture.mmd).
