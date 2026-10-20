# Database Schema Visualizer

Parses a practical subset of SQL `CREATE TABLE` statements and creates a Mermaid ER diagram plus a self-contained HTML viewer.

## Usage
```bash
pip install -r requirements.txt
python src/schema_to_mermaid.py sample/schema.sql --output outputs/schema.mmd --html outputs/schema.html
```

The HTML file loads Mermaid from its public CDN when opened in a browser. The `.mmd` output remains usable offline in Mermaid-capable editors.
