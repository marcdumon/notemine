import os

import anthropic
from openai import OpenAI


def complete(backend: str, system: str, user: str, config: dict) -> str:
    """Return a raw string completion from the chosen backend.

    Args:
        backend: 'ollama' or 'claude'
        system: system prompt string
        user: user prompt string
        config: full config dict from load_config()
    """
    if backend == 'ollama':
        cfg = config['ollama']
        client = OpenAI(base_url=cfg['base_url'], api_key='ollama')
        response = client.chat.completions.create(
            model=cfg['model'],
            messages=[
                {'role': 'system', 'content': system},
                {'role': 'user', 'content': user},
            ],
            temperature=cfg['temperature'],
            max_tokens=cfg['max_tokens'],
            response_format={'type': 'json_object'},
            extra_body={'options': {'num_ctx': cfg['num_ctx']}},
        )
        return response.choices[0].message.content

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
        return response.content[0].text

    else:
        raise ValueError(f'Unknown backend: {backend!r}. Use "ollama" or "claude".')
