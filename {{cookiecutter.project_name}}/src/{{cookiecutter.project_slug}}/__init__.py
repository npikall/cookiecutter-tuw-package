"""{{ cookiecutter.project_slug }}: Package to do ..."""

import importlib.metadata

__version__ = importlib.metadata.version(__name__)

NAME = "{{ cookiecutter.project_slug }}"


def main(name: str = NAME) -> None:
    """Entrypoint for the CLI."""
    print(f"Hello from {name}")
