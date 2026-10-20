import argparse, html, re
from pathlib import Path

CREATE_RE=re.compile(r"create\s+table\s+([`\w]+)\s*\((.*?)\)\s*;",re.I|re.S)
FK_RE=re.compile(r"foreign\s+key\s*\(([^)]+)\)\s*references\s+([`\w]+)\s*\(([^)]+)\)",re.I)
COL_RE=re.compile(r"^\s*([`\w]+)\s+([a-zA-Z]+(?:\s*\([^)]*\))?)",re.I)

def parse_schema(sql):
    tables={}
    rels=[]
    for tm in CREATE_RE.finditer(sql):
        table=tm.group(1).strip("`")
        body=tm.group(2)
        cols=[]
        for part in re.split(r",\s*(?![^()]*\))",body):
            fk=FK_RE.search(part)
            if fk:
                rels.append((table,fk.group(1).strip("` "),fk.group(2).strip("`"),fk.group(3).strip("` ")))
                continue
            cm=COL_RE.match(part)
            if cm and not re.match(r"^(primary|unique|constraint|foreign)\b",part.strip(),re.I):
                cols.append((cm.group(1).strip("`"),cm.group(2).replace(" ","_")))
        tables[table]=cols
    return tables,rels

def mermaid(tables, rels):
    lines=["erDiagram"]
    for t,cols in tables.items():
        lines.append(f"    {t} {{")
        for c,typ in cols:
            lines.append(f"        {typ} {c}")
        lines.append("    }")
    for src,src_col,dst,dst_col in rels:
        lines.append(f'    {dst} ||--o{{ {src} : "{dst_col} to {src_col}"')
    return "\n".join(lines)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("sql"); ap.add_argument("--output",default="schema.mmd"); ap.add_argument("--html",default="schema.html")
    a=ap.parse_args(); sql=Path(a.sql).read_text(encoding="utf-8")
    m=mermaid(*parse_schema(sql))
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(m,encoding="utf-8")
    page=f"""<!doctype html><meta charset="utf-8"><title>Schema Diagram</title>
<script type="module">import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';mermaid.initialize({{startOnLoad:true}});</script>
<pre class="mermaid">{html.escape(m)}</pre>"""
    Path(a.html).parent.mkdir(parents=True,exist_ok=True); Path(a.html).write_text(page,encoding="utf-8")

if __name__=="__main__": main()
