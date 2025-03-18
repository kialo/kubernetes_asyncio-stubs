# kubernetes_asyncio-stubs

Python type stubs for the [Kubernetes API client](https://github.com/tomplus/kubernetes_asyncio.git).
The code has been forked from [MaterializeInc/kubernetes-stubs](https://github.com/MaterializeInc/kubernetes-stubs.git).

At Kialo, we only have a single Kubernetes version in use at each time.
For a simplified release process, we release new stubs versions only for that version.
See tags for available list.

## Installation

```bash
pip install git+https://github.com/kialo/kubernetes_asyncio-stubs.git@v29.0.1
```

Alternatively, declare it as a dependency in your `pyproject.toml`.

poetry:

```toml
[tool.poetry.dependencies]
kubernetes-asyncio-stubs = { rev = "29.0.1", git = "https://github.com/kialo/kubernetes_asyncio-stubs" }
```

uv:

```toml
[tool.uv]
dev-dependencies = [
  "kubernetes_asyncio-stubs @ git+https://github.com/kialo/kubernetes_asyncio-stubs.git@29.0.1",
]
```

Remember to change the version number accordingly.

## Update development dependencies

Dev dependencies are currently only pinned via uv's lock file. You can upgrade them via:

```bash
uv sync --upgrade
```

## Development

These stubs are not complete, and in some cases may be incorrect.

Annotations for base files are stored under `codegen/base/`.

To (re-) generate the stubs for a (new) version of the Kubernetes API client, run:

1. Update `kubernetes_asyncio` submodule to target release
2. Update version in `pyproject.toml`
3. Generate API models: `uv run codegen ${target-version}`
4. Commit changes
5. Release new tag: `git tag v${version}; git push v${version}`
