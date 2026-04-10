import yaml


def load_ground_truth(path: str) -> dict[str, dict]:
    """Load ground_truth.yaml and return a dict keyed by filename.

    Returns:
        {filename: {'summary': str, 'tags': list[str], 'entities': list[dict]}}
    """
    with open(path, encoding='utf-8') as f:
        entries = yaml.safe_load(f)
    return {e['file']: e for e in entries}
