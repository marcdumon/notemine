# Notemine MVP Plan

## Context
Build an exploratory proof-of-concept that enriches Obsidian-style Markdown notes with three
independent LLM tasks (NER, tags, summary). Goal: compare quality across two backends
(local Ollama and Claude API) against curated ground truth in
`data/index_ner_tags_summary.md`, running each task in isolation through its own notebook so
prompts and models can be iterated task-by-task.

Nothing here is production architecture. Everything can change after the first runs.

---

## Actual Repo State

Project root: `/mnt/Dev/active_python_projects/notemine/`

Already exists:
- `src/notemine/` — package directory (contents unknown; check before overwriting)
- `notebooks/` — directory exists
- `data/` — 20 sample `.md` notes + `data/index_ner_tags_summary.md` present

Does **not** exist yet:
- `prompts/` — needs to be created
- `config.toml`
- `src/notemine/config.py`, `llm.py`, `frontmatter_io.py`, `ground_truth.py`, `tasks.py`

`pyproject.toml` and `main.py` exist and need modification.

---

## Component Flow

```
config.toml
    │
    ▼
config.load_config()
    │
    ├──► frontmatter_io ──► .md notes (data/*.md)
    │         │                  ▲
    │         │           reset_vault() strips notemine key
    │         │
    ├──► ground_truth.parse_index() ──► data/index_ner_tags_summary.md
    │
    └──► tasks.run_ner/run_tags/run_summary()
              │
              ├── reads prompts/ner.txt (tags.txt / summary.txt)
              │
              └──► llm.complete(backend, system, user, config)
                        │
                        ├── Ollama: OpenAI client → http://localhost:11434/v1
                        └── Claude: anthropic.Anthropic() → Anthropic API
```

Notebooks wire all of this together: load → run both backends → compare vs ground truth → (optional) write back.

---

## Project Structure to Create

```
config.toml
.env                               # ANTHROPIC_API_KEY (gitignored)
prompts/
  ner.txt
  tags.txt
  summary.txt
src/notemine/
  __init__.py
  config.py
  llm.py
  frontmatter_io.py
  ground_truth.py
  tasks.py
notebooks/
  01_ner.ipynb
  02_tags.ipynb
  03_summary.ipynb
main.py                            # replace stub with reset CLI
```

---

## Dependencies to Add

```
uv add openai anthropic python-frontmatter
```

`python-dotenv`, `pandas`, `ipykernel` already present. `tomllib` is stdlib in 3.11+.
Also update `pyproject.toml` `name` from `0-python-project-template` to `notemine`.

Add `.env` to `.gitignore`.

---

## config.toml

```toml
[ollama]
model = "llama3.2"
base_url = "http://localhost:11434/v1"
temperature = 0.1
num_ctx = 8192
max_tokens = 2000

[claude]
model = "claude-sonnet-4-6"
temperature = 0.1
max_tokens = 2000

[vault]
path = "./data"
ground_truth = "./data/index_ner_tags_summary.md"
```

---

## Prompts

System prompt (hardcoded in `tasks.py`):
```
You are a precise information extraction assistant. Return valid JSON only.
```

**`prompts/ner.txt`**
```
Extract all named entities from the following note. Return JSON with this exact structure:
{"entities": [[entity_text, entity_type], ...]}

Entity types: PER (person), ORG (organization), LOC (location), DATE (date/time expression),
PROD (product/technology), MISC (other notable named entity).
Keep entity text in the source language of the note.

Note content:
{content}
```

**`prompts/tags.txt`**
```
Generate 5-10 topic tags for the following note. Return JSON with this exact structure:
{"tags": ["tag-one", "tag-two", ...]}

Tags must be lowercase, hyphenated where multi-word, in the source language of the note.

Note content:
{content}
```

**`prompts/summary.txt`**
```
Summarize the following note as 2-3 bullet points. Return JSON with this exact structure:
{"summary": ["First key point as a complete sentence.", "Second key point.", ...]}

Write each bullet in the source language of the note.

Note content:
{content}
```

**Language note:** Ground truth in `data/index_ner_tags_summary.md` uses the note's source
language (e.g. Dutch entities stay Dutch). Prompts above match this. To switch to always-English,
edit the three prompt files only.

---

## Module Implementations

### `src/notemine/config.py`
```python
import tomllib

def load_config(path: str = "config.toml") -> dict:
    with open(path, "rb") as f:
        return tomllib.load(f)
```

### `src/notemine/llm.py`
```python
import os
from openai import OpenAI
import anthropic

def complete(backend: str, system: str, user: str, config: dict) -> str:
    if backend == "ollama":
        cfg = config["ollama"]
        client = OpenAI(base_url=cfg["base_url"], api_key="ollama")
        resp = client.chat.completions.create(
            model=cfg["model"],
            messages=[{"role": "system", "content": system},
                      {"role": "user", "content": user}],
            temperature=cfg["temperature"],
            max_tokens=cfg["max_tokens"],
            extra_body={"options": {"num_ctx": cfg["num_ctx"]}},
            response_format={"type": "json_object"},
        )
        return resp.choices[0].message.content
    elif backend == "claude":
        cfg = config["claude"]
        client = anthropic.Anthropic()          # reads ANTHROPIC_API_KEY from env
        resp = client.messages.create(
            model=cfg["model"],
            system=system,
            messages=[{"role": "user", "content": user}],
            temperature=cfg["temperature"],
            max_tokens=cfg["max_tokens"],
        )
        return resp.content[0].text
    else:
        raise ValueError(f"Unknown backend: {backend!r}")
```

### `src/notemine/frontmatter_io.py`
```python
import os, frontmatter

def load_note(path: str) -> frontmatter.Post:
    with open(path, encoding="utf-8") as f:
        return frontmatter.load(f)

def save_note(path: str, post: frontmatter.Post) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(frontmatter.dumps(post))

def reset_note(path: str) -> None:
    post = load_note(path)
    post.metadata.pop("notemine", None)
    save_note(path, post)

def reset_vault(vault: str) -> int:
    count = 0
    for fname in os.listdir(vault):
        if fname.endswith(".md") and not fname.startswith("index_"):
            reset_note(os.path.join(vault, fname))
            count += 1
    return count
```

### `src/notemine/ground_truth.py`
```python
import re

def parse_index(path: str) -> dict[str, dict]:
    """Parse index_ner_tags_summary.md → {filename: {summary, tags, ner}}"""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    # Split on note sections "## N. filename" headers
    sections = re.split(r'^## \d+\.\s+', text, flags=re.MULTILINE)
    result = {}
    for section in sections[1:]:           # first split is preamble
        lines = section.strip().splitlines()
        filename = lines[0].strip()
        body = "\n".join(lines[1:])
        # Extract NER block
        ner_match = re.search(r'### NER\s*(.*?)(?=###|\Z)', body, re.DOTALL)
        # Extract Tags block
        tags_match = re.search(r'### Tags\s*(.*?)(?=###|\Z)', body, re.DOTALL)
        # Extract Summary block
        summary_match = re.search(r'### Summary\s*(.*?)(?=###|\Z)', body, re.DOTALL)
        result[filename] = {
            "ner": _parse_ner(ner_match.group(1) if ner_match else ""),
            "tags": _parse_tags(tags_match.group(1) if tags_match else ""),
            "summary": _parse_summary(summary_match.group(1) if summary_match else ""),
        }
    return result

def _parse_ner(block: str) -> list[tuple[str, str]]:
    return re.findall(r'\(([^,)]+),\s*([A-Z]+)\)', block)

def _parse_tags(block: str) -> list[str]:
    return re.findall(r'`([^`]+)`', block)

def _parse_summary(block: str) -> list[str]:
    bullets = re.findall(r'^[-*]\s+(.+)', block.strip(), re.MULTILINE)
    return bullets if bullets else [l.strip() for l in block.strip().splitlines() if l.strip()]
```

**Note:** The exact regex patterns in `ground_truth.py` must be validated against the actual
format of `data/index_ner_tags_summary.md` once that file is available. The above assumes:
- Entities formatted as `(Entity Text, TYPE)`
- Tags formatted as `` `tag-name` ``
- Summary as `- bullet` lines

### `src/notemine/tasks.py`
```python
import json, re

SYSTEM = "You are a precise information extraction assistant. Return valid JSON only."

def _load_prompt(task: str, content: str) -> str:
    with open(f"prompts/{task}.txt", encoding="utf-8") as f:
        return f.read().format(content=content)

def _parse_json(raw: str) -> dict:
    # Strip optional markdown fences
    cleaned = re.sub(r'^```(?:json)?\s*|\s*```$', '', raw.strip())
    return json.loads(cleaned)

def run_ner(backend: str, content: str, config: dict) -> list[list[str]]:
    from notemine.llm import complete
    from notemine.config import load_config
    user = _load_prompt("ner", content)
    raw = complete(backend, SYSTEM, user, config)
    return _parse_json(raw)["entities"]

def run_tags(backend: str, content: str, config: dict) -> list[str]:
    from notemine.llm import complete
    user = _load_prompt("tags", content)
    raw = complete(backend, SYSTEM, user, config)
    return _parse_json(raw)["tags"]

def run_summary(backend: str, content: str, config: dict) -> list[str]:
    from notemine.llm import complete
    user = _load_prompt("summary", content)
    raw = complete(backend, SYSTEM, user, config)
    return _parse_json(raw)["summary"]
```

### `main.py` (replace stub)
```python
import sys
from dotenv import load_dotenv
from notemine.config import load_config
from notemine.frontmatter_io import reset_vault

def main():
    load_dotenv()
    config = load_config()
    if len(sys.argv) > 1 and sys.argv[1] == "reset":
        vault = config["vault"]["path"]
        count = reset_vault(vault)
        print(f"Reset {count} notes in {vault!r}")
    else:
        print("Usage: python main.py reset")

if __name__ == "__main__":
    main()
```

---

## Notebook Template

All three notebooks follow the same pattern (swap task name):

**Cell 1 — Setup**
```python
import os, glob, frontmatter
import pandas as pd
from dotenv import load_dotenv
from notemine.config import load_config
from notemine.ground_truth import parse_index
from notemine.tasks import run_ner   # or run_tags / run_summary

load_dotenv()
config = load_config()
gt = parse_index(config["vault"]["ground_truth"])
note_paths = [p for p in glob.glob(f"{config['vault']['path']}/*.md")
              if not os.path.basename(p).startswith("index_")]
```

**Cell 2 — Run both backends**
```python
results = []
for path in note_paths:
    fname = os.path.basename(path)
    post = frontmatter.load(path)
    content = post.content
    ollama_result = run_ner("ollama", content, config)
    claude_result  = run_ner("claude", content, config)
    results.append({
        "filename": fname,
        "ground_truth": gt.get(fname, {}).get("ner"),
        "ollama": ollama_result,
        "claude": claude_result,
    })
```

**Cell 3 — Compare**
```python
df = pd.DataFrame(results)
display(df)
```

**Cell 4 — (Optional) Write back to frontmatter**
```python
from notemine.frontmatter_io import load_note, save_note

for row in results:
    path = os.path.join(config["vault"]["path"], row["filename"])
    post = load_note(path)
    nm = post.metadata.setdefault("notemine", {})
    nm.setdefault("ner", {})
    nm["ner"]["ollama"] = row["ollama"]
    nm["ner"]["claude"] = row["claude"]
    save_note(path, post)
print("Written.")
```

`02_tags.ipynb` and `03_summary.ipynb` are identical with `run_tags`/`"tags"` and
`run_summary`/`"summary"` substituted.

---

## Frontmatter Schema

```yaml
notemine:
  ner:
    ollama: [[Sam Altman, PER], [OpenAI, ORG]]
    claude: [[Sam Altman, PER], [OpenAI, ORG]]
  tags:
    ollama: [ai, language-models]
    claude: [ai, language-models]
  summary:
    ollama: ["OpenAI CEO Sam Altman announced..."]
    claude: ["OpenAI CEO Sam Altman announced..."]
```

`reset_vault()` pops only the top-level `notemine` key; all original fields are untouched.

---

## Implementation Order

1. `pyproject.toml` — rename project, add `openai`, `anthropic`, `python-frontmatter`; add `.env` to `.gitignore`
2. `config.toml` — create at project root
3. `prompts/ner.txt`, `prompts/tags.txt`, `prompts/summary.txt`
4. `src/notemine/__init__.py` (empty)
5. `src/notemine/config.py`
6. `src/notemine/llm.py`
7. `src/notemine/frontmatter_io.py`
8. `src/notemine/ground_truth.py` — **validate regexes against actual index file before finalizing**
9. `src/notemine/tasks.py`
10. `main.py` — replace stub
11. `notebooks/01_ner.ipynb`, `02_tags.ipynb`, `03_summary.ipynb`

---

## Verification

1. `uv sync` — confirm no dependency errors
2. `python main.py reset` — should print `Reset 0 notes` (or N if data is present)
3. Place `data/*.md` and `data/index_ner_tags_summary.md`
4. Open `01_ner.ipynb`, run all cells — confirm DataFrame with 3 columns appears
5. Inspect ground truth column vs both backends; iterate prompt if needed
6. Repeat for `02_tags.ipynb` and `03_summary.ipynb`
7. Run optional write-back cell, then `python main.py reset` — confirm `notemine` key gone

---

## Critical Files

| File | Action |
|---|---|
| `pyproject.toml` | Modify — add `openai`, `anthropic`, `python-frontmatter`; rename project |
| `.gitignore` | Modify — add `.env` |
| `config.toml` | Create |
| `prompts/ner.txt`, `tags.txt`, `summary.txt` | Create (new dir) |
| `src/notemine/__init__.py` | Keep/create (empty) |
| `src/notemine/config.py` | Create |
| `src/notemine/llm.py` | Create |
| `src/notemine/frontmatter_io.py` | Create |
| `src/notemine/ground_truth.py` | Create (validate regexes against actual index file) |
| `src/notemine/tasks.py` | Create |
| `main.py` | Modify — replace stub with reset CLI |
| `notebooks/01_ner.ipynb` | Create |
| `notebooks/02_tags.ipynb` | Create |
| `notebooks/03_summary.ipynb` | Create |

**Before implementing:** read `data/index_ner_tags_summary.md` to confirm the NER/tags/summary
section format so `ground_truth.py` regexes match reality. Also check existing `src/notemine/`
contents to avoid overwriting any work already done.
