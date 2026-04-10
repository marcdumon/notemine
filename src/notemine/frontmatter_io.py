from glob import glob

import frontmatter


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
        print(f'Resetting {path}...')
        post = load_note(path)
        if 'notemine' in post.metadata:
            del post.metadata['notemine']
            save_note(path, post)
            count += 1
    return count
