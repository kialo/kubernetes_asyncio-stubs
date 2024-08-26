import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1FlowSchema:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V1FlowSchemaSpec]
    status: typing.Optional[kubernetes_asyncio.client.V1FlowSchemaStatus]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes_asyncio.client.V1FlowSchemaSpec] = ...,
        status: typing.Optional[kubernetes_asyncio.client.V1FlowSchemaStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1FlowSchemaDict: ...

class V1FlowSchemaDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V1FlowSchemaSpecDict]
    status: typing.Optional[kubernetes_asyncio.client.V1FlowSchemaStatusDict]
