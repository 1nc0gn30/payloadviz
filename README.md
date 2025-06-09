# PayloadViz: CLI Payload Visualizer for Pentesters

![PayloadViz](https://img.shields.io/badge/built_with-python-blue?style=flat-square)
![Graphviz](https://img.shields.io/badge/graphviz-enabled-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

---

## 🔍 What Is PayloadViz?

**PayloadViz** is a CLI tool that helps you **visualize how hacking payloads flow and execute** — perfect for beginners learning about exploits and pros who want a clean view of what's happening inside a payload.

It takes input like XSS, SQLi, or LFI payloads and:

* Automatically detects the type
* Tokenizes the payload
* Generates a flowchart/tree of execution using **Graphviz**, **Rich**, or **Mermaid**
* Exports to **SVG**, **Markdown**, or prints a tree in your terminal

---

## 🧠 Why It Matters

Most hacking tutorials throw raw payloads at learners with no explanation. This tool fixes that. Whether you're:

* Studying attack vectors
* Teaching infosec
* Red teaming and want fast insight
* Building payloads yourself

...**this tool gives you clarity.**

---

## 🚀 Quick Start

### 1. Install

```bash
# Clone it
git clone https://github.com/1nc0gn30/payloadviz && cd payloadviz

# Create virtual environment (optional)
python3 -m venv venv && source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install as CLI tool
pip install -e .
```

### 2. Run

```bash
payloadviz "<script>alert('XSS')</script>" --export tree

payloadviz "' OR '1'='1 --" --export svg

payloadviz "../../etc/passwd" --export md
```

---

## ✨ Output Types

| Output Option   | Description                   |
| --------------- | ----------------------------- |
| `--export tree` | Terminal tree (rich CLI)      |
| `--export svg`  | Graphviz SVG flow             |
| `--export md`   | Mermaid Markdown chart        |
| *(none)*        | Print raw Graphviz dot syntax |

---

## 🧰 Supported Payloads

* ✅ XSS (`<script>`, `onerror`, etc)
* ✅ SQLi (`' OR 1=1`, `UNION SELECT`)
* ✅ LFI (`../`, `include`, etc)
* ⏳ More coming soon: SSTI, XXE, RCE...

---

## 🛠 Project Structure

```
payloadviz/
├── cli/              # CLI entry point
├── core/             # Detection, parsing, visualizing
├── utils/            # Export functions
├── payloads/         # Sample payloads
├── requirements.txt
├── setup.py
└── README.md
```

---

## 💡 Roadmap

* [x] Graphviz visualizer
* [x] Mermaid Markdown exporter
* [x] Tree-based CLI preview
* [ ] Web-based renderer (WASM or Flask)
* [ ] Plugin payloads from external JSON
* [ ] Parse + visualize nested JS/RCE logic

---

## 👨‍💻 Author

**Neal Frazier** — [nealfrazier.tech](https://nealfrazier.tech)
GitHub: [@1nc0gn30](https://github.com/1nc0gn30)

> Builder. Breaker. Visual thinker. I make tools that make knowledge visible.

---

## 📄 License

MIT. Use it, fork it, improve it — just give credit where it’s due.

---

## 🙌 Contributions Welcome

Found a bug? Got an idea? Wanna support more payload types? Fork it and feel free to customize how you'd like it for your own workflow or creativity.

---

## ⭐ Star This Repo If You Want More Hacking Tools Like This
