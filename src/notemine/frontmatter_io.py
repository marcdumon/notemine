import logging
from glob import glob

import frontmatter

logger = logging.getLogger(__name__)


def load_note(path: str) -> frontmatter.Post:
    """Load a markdown file and parse its YAML frontmatter."""
    return frontmatter.load(path)


def save_note(path: str, post: frontmatter.Post) -> None:
    """Write a Post back to disk, preserving body and frontmatter structure."""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))


def reset_note(path: str) -> None:
    """Strip the 'notemine' key from a note's frontmatter."""
    post = load_note(path)
    if 'notemine' in post.metadata:
        del post.metadata['notemine']
        save_note(path, post)


def reset_vault(vault: str) -> int:
    """Strip 'notemine' frontmatter from all .md files in vault. Returns count reset."""
    paths = glob(f'{vault}/**/*.md', recursive=True)
    count = 0
    for path in paths:
        logger.info('Resetting %s', path)
        post = load_note(path)
        if 'notemine' in post.metadata:
            del post.metadata['notemine']
            save_note(path, post)
            count += 1
    return count


def strip_tags_vault(vault: str) -> int:
    """Remove the 'tags' key from frontmatter of all .md files in vault. Returns count modified."""
    paths = glob(f'{vault}/**/*.md', recursive=True)
    count = 0
    for path in paths:
        post = load_note(path)
        if 'tags' in post.metadata:
            del post.metadata['tags']
            save_note(path, post)
            logger.info('Stripped tags: %s', path)
            count += 1
    return count
