import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1FlowSchemaList:
    api_version: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V1FlowSchema]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1FlowSchema],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1FlowSchemaListDict: ...

class V1FlowSchemaListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V1FlowSchemaDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMetaDict]
