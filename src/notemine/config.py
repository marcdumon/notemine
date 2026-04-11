import tomllib
from typing import TypedDict


class OllamaConfig(TypedDict):
    """Ollama backend settings."""
    model: str
    base_url: str
    temperature: float
    num_ctx: int
    max_tokens: int


class ClaudeConfig(TypedDict):
    """Anthropic Claude backend settings."""
    model: str
    temperature: float
    max_tokens: int


class RunConfig(TypedDict):
    """Default run settings."""
    backend: str


class VaultConfig(TypedDict):
    """Vault filesystem settings."""
    path: str
    ground_truth: str
    prompts_dir: str


class Config(TypedDict):
    """Full application config as loaded from config.toml."""
    ollama: OllamaConfig
    claude: ClaudeConfig
    run: RunConfig
    vault: VaultConfig


def load_config(path: str = 'config.toml') -> Config:
    """Load config.toml and return as a typed Config dict."""
    with open(path, 'rb') as f:
        return tomllib.load(f)  # type: ignore[return-value]
