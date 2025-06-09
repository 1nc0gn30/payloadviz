from graphviz import Digraph
from rich import print

def export_svg(dot: Digraph, out_path: str):
    dot.format = 'svg'
    dot.render(out_path, view=False)
    print(f"[green]SVG exported:[/] {out_path}.svg")

def export_md(nodes: list, out_path: str):
    lines = ["```mermaid", "flowchart LR"]
    for i, n in enumerate(nodes):
        lines.append(f"    N{i}[\"{n['value']}\"]")
        if i>0:
            lines.append(f"    N{i-1} --> N{i}")
    lines.append("```")
    with open(out_path, 'w') as f:
        f.write('\n'.join(lines))
    print(f"[green]Markdown exported:[/] {out_path}")

def export_tree(nodes: list):
    for i, n in enumerate(nodes):
        prefix = '└─ ' if i == len(nodes)-1 else '├─ '
        print(f"{prefix}[blue]{n['type']}[/]: {n['value']}")
