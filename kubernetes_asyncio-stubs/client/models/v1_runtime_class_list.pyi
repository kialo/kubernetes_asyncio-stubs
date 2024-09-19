import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1RuntimeClassList:
    api_version: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V1RuntimeClass]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1RuntimeClass],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1RuntimeClassListDict: ...

class V1RuntimeClassListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V1RuntimeClassDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMetaDict]
