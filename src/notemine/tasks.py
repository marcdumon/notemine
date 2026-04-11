import json
from pathlib import Path
from typing import Any

from notemine.config import Config
from notemine.llm import complete

_SYSTEM = 'You are a precise information extraction assistant. Return valid JSON only. No markdown fences.'


def _load_prompt(prompts_dir: str, task: str) -> str:
    """Load prompt template from prompts/<task>.txt."""
    return Path(prompts_dir, f'{task}.txt').read_text(encoding='utf-8')


def _parse_json(raw: str) -> dict[str, Any]:
    """Strip optional markdown fences and parse JSON."""
    raw = raw.strip()
    if raw.startswith('```'):
        raw = raw.split('\n', 1)[-1].rsplit('```', 1)[0].strip()
    return json.loads(raw)


def run_ner(backend: str, content: str, config: Config) -> list[list[str]]:
    """Run NER on note content. Returns list of [entity_text, entity_type] pairs."""
    template = _load_prompt(config['vault']['prompts_dir'], 'ner')
    user = template.format(content=content)
    raw = complete(backend, _SYSTEM, user, config)
    result = _parse_json(raw)
    return result['entities']


def run_tags(backend: str, content: str, config: Config) -> list[str]:
    """Run tag generation on note content. Returns list of tag strings."""
    template = _load_prompt(config['vault']['prompts_dir'], 'tags')
    user = template.format(content=content)
    raw = complete(backend, _SYSTEM, user, config)
    result = _parse_json(raw)
    return result['tags']


def run_summary(backend: str, content: str, config: Config) -> list[str]:
    """Run summarisation on note content. Returns list of sentence strings."""
    template = _load_prompt(config['vault']['prompts_dir'], 'summary')
    user = template.format(content=content)
    raw = complete(backend, _SYSTEM, user, config)
    result = _parse_json(raw)
    return result['summary']
