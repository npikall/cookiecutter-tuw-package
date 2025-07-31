# Readme

TODO: Add documentation!

## Development

This project uses `uv` for package management and development tasks and `Just` for task automation.
To install `Just`, follow the instructions in the [Just documentation](https://github.com/casey/just).

To install `uv`, you can use the following command:

```bash
pip install uv
```

or check the [uv documentation](https://docs.astral.sh/uv/getting-started/installation/)

In order to use the Pre-commit hooks, run:

```bash
pre-commit install --hook-type commit-msg --hook-type pre-push
```

The Pre-commit Hooks will lint and format your code and your commit messages will be checked if
they adhere to the `Conventional Commit` Standards. This allows the use of tools for automatic
bumping and changlog writing.
