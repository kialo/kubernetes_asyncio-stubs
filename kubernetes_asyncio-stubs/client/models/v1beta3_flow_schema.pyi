import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta3FlowSchema:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V1beta3FlowSchemaSpec]
    status: typing.Optional[kubernetes_asyncio.client.V1beta3FlowSchemaStatus]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes_asyncio.client.V1beta3FlowSchemaSpec] = ...,
        status: typing.Optional[
            kubernetes_asyncio.client.V1beta3FlowSchemaStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta3FlowSchemaDict: ...

class V1beta3FlowSchemaDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V1beta3FlowSchemaSpecDict]
    status: typing.Optional[kubernetes_asyncio.client.V1beta3FlowSchemaStatusDict]
