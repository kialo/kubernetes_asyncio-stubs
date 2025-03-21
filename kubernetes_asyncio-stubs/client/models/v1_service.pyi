import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1Service:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1ServiceSpec
    status: kubernetes_asyncio.client.V1ServiceStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes_asyncio.client.V1ServiceSpec] = ...,
        status: typing.Optional[kubernetes_asyncio.client.V1ServiceStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ServiceDict: ...

class V1ServiceDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1ServiceSpecDict
    status: kubernetes_asyncio.client.V1ServiceStatusDict
