# Database Schema Visualizer

Parses a practical subset of SQL CREATE TABLE statements and creates a Mermaid ER diagram plus a self-contained HTML viewer.

[Research notes](docs/RESEARCH.md) · [Architecture](docs/ARCHITECTURE.md) · [Execution record](docs/RESULTS.md) · [Project site](docs/index.html)

---

## Research context

How accurately can basic SQL schema definitions be translated into human-readable entity diagrams?

The repository provides an inspectable implementation of **sql-to-mermaid er diagrams**. It is an exploratory engineering project; broader effectiveness and practical deployment require further study.

## Implemented capabilities

- SQL-to-Mermaid ER diagrams

## Architecture

```mermaid
flowchart LR
    A["schema.sql"] --> B["schema_to_mermaid.py"]
    B --> C["schema.html, schema.mmd"]
```

The diagram is a simplified view of the supplied implementation. Detailed modules and interface assumptions are in [architecture notes](docs/ARCHITECTURE.md).

## Run locally

**Environment:** Python 3.11+ is the documented baseline. Install optional services or hardware drivers when required.

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

Run the following commands from the repository root:

```bash
python src/schema_to_mermaid.py sample/schema.sql --output outputs/schema.mmd --html outputs/schema.html
```

**Input:** `sample/schema.sql`

## Results

**Executed locally** with the included input files. This is an implementation check, not an independently validated benchmark.

![Output from the local execution](assets/result.svg)


**Execution evidence:** [Full command transcript](results/execution.txt) · [Inputs and checksums](results/execution.json)

**Saved outputs**

- [`schema.html`](results/artifacts/schema.html)
- [`schema.mmd`](results/artifacts/schema.mmd)

The values above come from the bundled fixtures. Model scores, simulated costs, and resource-use estimates should not be interpreted as real-world deployment results.

## Source structure

- [`src/schema_to_mermaid.py`](src/schema_to_mermaid.py)

Documentation is in [`docs/`](docs/). Bundled inputs remain in their original folders. The original project instructions are archived in [`docs/ORIGINAL_README.md`](docs/ORIGINAL_README.md).

## Limits and next research steps

- Results shown here are from local bundled inputs; they are not published research findings or evidence of external deployment.
- Validate domain assumptions and compare against a documented baseline before making performance or reliability claims.
- Extend testing to larger, independently sourced datasets and report reproducibility, failures and relevant ethical risks.

For the methodology and evaluation design, see [the research brief](docs/RESEARCH.md).

## License

See [`LICENSE`](LICENSE). No affiliation, patent, publication, production deployment or independent endorsement is implied.
