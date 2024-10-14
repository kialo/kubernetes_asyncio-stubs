import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1StorageClassList:
    api_version: str
    items: list[kubernetes_asyncio.client.V1StorageClass]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1StorageClass],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1StorageClassListDict: ...

class V1StorageClassListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes_asyncio.client.V1StorageClassDict]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMetaDict
