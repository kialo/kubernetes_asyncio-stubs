import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta3FlowSchemaList:
    api_version: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V1beta3FlowSchema]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1beta3FlowSchema],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta3FlowSchemaListDict: ...

class V1beta3FlowSchemaListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V1beta3FlowSchemaDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMetaDict]
