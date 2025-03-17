import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PriorityClassList:
    api_version: str
    items: list[kubernetes_asyncio.client.V1PriorityClass]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1PriorityClass],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PriorityClassListDict: ...

class V1PriorityClassListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes_asyncio.client.V1PriorityClassDict]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMetaDict
