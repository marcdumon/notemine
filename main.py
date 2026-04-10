import sys

from dotenv import load_dotenv

from notemine.config import load_config
from notemine.frontmatter_io import reset_vault, strip_tags_vault

load_dotenv()

USAGE = 'Usage: python main.py reset|strip-tags'


def main() -> None:
    """CLI entry point. Currently supports: reset."""
    if len(sys.argv) < 2:
        print(USAGE)
        sys.exit(1)

    command = sys.argv[1]

    if command == 'reset':
        config = load_config()
        vault = config['vault']['path']
        count = reset_vault(vault)
        print(f'Reset {count} notes in {vault}')
    elif command == 'strip-tags':
        config = load_config()
        vault = config['vault']['path']
        count = strip_tags_vault(vault)
        print(f'Stripped tags from {count} notes in {vault}')
    else:
        print(f'Unknown command: {command!r}\n{USAGE}')
        sys.exit(1)


if __name__ == '__main__':
    main()
