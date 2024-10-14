import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1RoleList:
    api_version: str
    items: list[kubernetes_asyncio.client.V1Role]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1Role],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1RoleListDict: ...

class V1RoleListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes_asyncio.client.V1RoleDict]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMetaDict
