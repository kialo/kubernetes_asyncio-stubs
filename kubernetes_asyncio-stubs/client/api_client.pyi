from typing import Any, Iterable, Optional, Protocol, Self, Type, TypeVar

from .configuration import Configuration

_T = TypeVar("_T")

class Response(Protocol):
    data: str

class ApiClient:
    NATIVE_TYPES_MAPPING: dict[str, Any] = ...
    PRIMITIVE_TYPES: tuple[Any] = ...
    def __init__(self, configuration: Optional[Configuration] = ...) -> None: ...
    async def __aenter__(self) -> Self: ...
    async def __aexit__(
        self, exc_type: Any, exc_value: Any, traceback: Any
    ) -> None: ...
    async def close(self) -> None: ...
    async def call_api(
        self,
        resource_path: str,
        method: str,
        path_params: dict[str, Any] | None | None = ...,
        query_params: list[Any] | None = ...,
        header_params: dict[str, Any] | None = ...,
        body: dict[str, Any] | None = ...,
        post_params: dict[str, Any] | None = ...,
        files: dict[str, str] | None = ...,
        response_types_map: dict[int, Any] | None = ...,
        auth_settings: list[str] | None = ...,
        async_req: bool | None = ...,
        _return_http_data_only: bool | None = ...,
        collection_formats: dict[str, Any] | None = ...,
        _preload_content: bool | None = ...,
        _request_timeout: int | tuple[Any] | None = ...,
        _host: str | None = ...,
        _request_auth: dict[str, Any] | None = ...,
    ) -> dict[str, Any]: ...
    def deserialize(self, response: Response, response_type: Type[_T]) -> _T: ...
    def sanitize_for_serialization(self, obj: Any) -> dict[Any, Any]: ...
    def select_header_accept(self, accepts: Iterable[str]) -> str: ...
