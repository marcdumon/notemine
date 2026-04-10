import tomllib


def load_config(path: str = 'config.toml') -> dict:
    """Load config.toml and return as a plain dict."""
    with open(path, 'rb') as f:
        return tomllib.load(f)
