import re

TYPE_PATTERNS = {
    'XSS': [r'<script', r'onerror=', r'alert\('],
    'SQLi': [r'--', r'\' OR ', r'UNION SELECT'],
    'LFI': [r'\.\./', r'\.php\?', r'include\('],
}

def detect_type(payload: str) -> str:
    p = payload.strip()
    for t, patterns in TYPE_PATTERNS.items():
        for pat in patterns:
            if re.search(pat, p, re.IGNORECASE):
                return t
    return 'GENERIC'
