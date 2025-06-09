# Payload Visualizer CLI

Visualize security payloads (XSS, SQLi, LFI) via Graphviz, Mermaid, or terminal preview.

## Install

```bash
pip install -e .
```

## Usage

payloadviz "<script>alert('XSS')</script>"
payloadviz "1' OR '1'='1" --export svg
payloadviz "../../etc/passwd" --export tree


---

### ✅ Next Steps
- Hook in `mermaid-cli` or web UI for `.md` files
- Add more detection rules, payload types
- Implement unit tests
- Document common payloads & parsing logic in `payloads/`
- Possibly expand to multi-payload pipelines

---

Let me know if you want me to step you through implementation, set up CI, doc styling, or bump into advanced features like interactive live preview or integration with pentest frameworks.
