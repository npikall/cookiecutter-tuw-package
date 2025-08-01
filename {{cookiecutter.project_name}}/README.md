# Readme

TODO: Add documentation!

## First Steps

After you have just used cookiecutter to create this repo, you might want to follow these steps:

1. Initialize a git repo
2. Run `just hooks`
3. Commit the initial state.
4. Run `just uv` to set up the virtual environment

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

or use the Justfile to do the same:

```bash
just hooks
```

The Pre-commit Hooks will lint and format your code and your commit messages will be checked if
they adhere to the `Conventional Commit` Standards. This allows the use of tools for automatic
bumping and changlog writing.

`commitizen` is such a tool. You can use it to automatically bump your repos version.

```bash
# Install
uv pip install commitizen

# Bump the repo
cz bump
```

Depending on the previously made commit types `commitizen` will be determining the the next version number,
which follows this pattern `<major>.<minor>.<patch>`

- type `feat` => Minor change
- type `fix` => Patch
- `<type>!` => Major change

As long as `major_version_zero = true` in the pyproject file no major version increment will be made.
