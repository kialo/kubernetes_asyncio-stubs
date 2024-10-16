import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NamespaceList:
    api_version: str
    items: list[kubernetes_asyncio.client.V1Namespace]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1Namespace],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1NamespaceListDict: ...

class V1NamespaceListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes_asyncio.client.V1NamespaceDict]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMetaDict
