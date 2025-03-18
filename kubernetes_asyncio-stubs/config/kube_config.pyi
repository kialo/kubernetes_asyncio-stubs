from typing import Any, Optional, TypedDict

from ..client import ApiClient, Configuration

KUBE_CONFIG_DEFAULT_LOCATION: str = ...

class Context(TypedDict):
    name: str
    context: dict[str, Any]

def list_kube_config_contexts(
    config_file: Optional[str] = ...,
) -> tuple[list[Context], Context]: ...
async def load_kube_config(
    config_file: Optional[str] = ...,
    context: Optional[str] = ...,
    client_configuration: Optional[Configuration] = ...,
    persist_config: bool = ...,
) -> None: ...
async def load_kube_config_from_dict(
    config_dict: dict[Any, Any] = ...,
    context: Optional[str] = ...,
    client_configuration: Optional[Configuration] = ...,
    persist_config: bool = ...,
    temp_file_path: Optional[str] = ...,
) -> None: ...
async def new_client_from_config(
    config_file: Optional[str] = ...,
    context: Optional[str] = ...,
    persist_config: bool = ...,
) -> ApiClient: ...
