import os

import anthropic
import ollama
from anthropic.types import TextBlock

from notemine.config import Config


def complete(backend: str, system: str, user: str, config: Config) -> str:
    """Return a raw string completion from the chosen backend.

    Args:
        backend: 'ollama' or 'claude'
        system: system prompt string
        user: user prompt string
        config: full config dict from load_config()
    """
    if backend == 'ollama':
        cfg = config['ollama']
        client = ollama.Client(host=cfg['base_url'])
        response = client.chat(
            model=cfg['model'],
            messages=[
                {'role': 'system', 'content': system},
                {'role': 'user', 'content': user},
            ],
            format='json',
            options={
                'temperature': cfg['temperature'],
                'num_predict': cfg['max_tokens'],
                'num_ctx': cfg['num_ctx'],
            },
        )
        return response.message.content or ''

    elif backend == 'claude':
        cfg = config['claude']
        client = anthropic.Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])
        response = client.messages.create(
            model=cfg['model'],
            system=system,
            messages=[{'role': 'user', 'content': user}],
            temperature=cfg['temperature'],
            max_tokens=cfg['max_tokens'],
        )
        text_blocks = [block.text for block in response.content if isinstance(block, TextBlock)]
        return ''.join(text_blocks)

    else:
        raise ValueError(f'Unknown backend: {backend!r}. Use "ollama" or "claude".')
