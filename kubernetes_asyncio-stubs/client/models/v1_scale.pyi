import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1Scale:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1ScaleSpec
    status: kubernetes_asyncio.client.V1ScaleStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes_asyncio.client.V1ScaleSpec] = ...,
        status: typing.Optional[kubernetes_asyncio.client.V1ScaleStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ScaleDict: ...

class V1ScaleDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1ScaleSpecDict
    status: kubernetes_asyncio.client.V1ScaleStatusDict
