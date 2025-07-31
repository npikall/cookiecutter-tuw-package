from {{ cookiecutter.project_slug }}._version import __commit__
from {{ cookiecutter.project_slug }}._version import __version__

name = "{{ cookiecutter.project_slug }}"

def main() -> None:
    print(f"Hello from {name}")
