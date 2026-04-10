# notemine

Enrich Obsidian-style Markdown notes with LLM-generated metadata (NER, tags, summary).

## Backends

- **Ollama** (local) — default
- **Claude** (Anthropic API) — requires `ANTHROPIC_API_KEY`

Configure models and paths in `config.toml`.

## Usage

```bash
python main.py reset   # strip notemine frontmatter from all notes in the vault
```

Exploration and evaluation live in `notebooks/`.
