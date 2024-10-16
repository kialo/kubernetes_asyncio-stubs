import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha2PodSchedulingContext:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1alpha2PodSchedulingContextSpec
    status: kubernetes_asyncio.client.V1alpha2PodSchedulingContextStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: kubernetes_asyncio.client.V1alpha2PodSchedulingContextSpec,
        status: typing.Optional[
            kubernetes_asyncio.client.V1alpha2PodSchedulingContextStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2PodSchedulingContextDict: ...

class V1alpha2PodSchedulingContextDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1alpha2PodSchedulingContextSpecDict
    status: kubernetes_asyncio.client.V1alpha2PodSchedulingContextStatusDict
