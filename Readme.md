# kubernetes_asyncio-stubs

Python type stubs for the [Kubernetes API client](https://github.com/borissmidt/kubernetes_asyncio.git).
The code has been forked from [MaterializeInc/kubernetes-stubs](https://github.com/MaterializeInc/kubernetes-stubs.git).
Stubs are contained in Git branches, which are named after the respective Kubernetes client version.

## Installation

```bash
pip install git+https://github.com/kialo/kubernetes_asyncio-stubs.git@v29.0.1
```

Alternatively, include the following line in your `pyproject.tml`:

```toml
kubernetes-asyncio-stubs = { rev = "29.0.1", git = "https://github.com/kialo/kubernetes_asyncio-stubs" }
```

Remember to change the version number accordingly.

## Development

These stubs are not complete, and in some cases may be incorrect.
Follow these steps to adapt or extend the stubs:

1. Include missing annotations in the base files under `codegen/base/`, preferably on the `master` branch.
2. Switch to a Git branch named after the `kubernetes_asyncio` version you are generating stubs for,
   and checkout the corresponding tag of the `kubernetes_asyncio` submodule.
3. Run `python codegen` to generate stubs from the Kubernetes OpenAPI spec.
