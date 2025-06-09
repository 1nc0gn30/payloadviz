from graphviz import Digraph
from rich import print
from utils.exporters import export_svg, export_md, export_tree

def visualize_payload(parsed: dict, payload_type: str, export: str):
    nodes = parsed['nodes']
    dot = Digraph(comment=payload_type)
    for i, n in enumerate(nodes):
        dot.node(str(i), f"{n['type']}:{n['value']}")
        if i > 0:
            dot.edge(str(i-1), str(i))
    if export == 'svg':
        export_svg(dot, f"out_{payload_type}.svg")
    elif export == 'md':
        export_md(nodes, f"out_{payload_type}.md")
    elif export == 'tree':
        export_tree(nodes)
    else:
        print(dot.source)
