import click
from core.detector import detect_type
from core.parser import parse_payload
from core.visualizer import visualize_payload

@click.command()
@click.argument('payload')
@click.option('--export', type=click.Choice(['svg','md','tree','dot']), default=None)
def main(payload, export):
    pt = detect_type(payload)
    parsed = parse_payload(payload, pt)
    visualize_payload(parsed, pt, export)

if __name__ == '__main__':
    main()
