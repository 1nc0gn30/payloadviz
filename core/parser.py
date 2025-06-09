from typing import List, Dict

def parse_payload(payload: str, payload_type: str) -> Dict:
    nodes = []
    if payload_type == 'XSS':
        if '<script' in payload:
            nodes.append({'type':'tag','value':'<script>'})
        if 'alert(' in payload:
            nodes.append({'type':'func','value':'alert()'})
    elif payload_type == 'SQLi':
        for part in payload.split():
            nodes.append({'type':'token','value':part})
    else:
        nodes.append({'type':'raw','value':payload})
    return {'type':payload_type, 'nodes':nodes}
