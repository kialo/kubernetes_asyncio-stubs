import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha3PodSchedulingContext:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1alpha3PodSchedulingContextSpec
    status: kubernetes_asyncio.client.V1alpha3PodSchedulingContextStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: kubernetes_asyncio.client.V1alpha3PodSchedulingContextSpec,
        status: typing.Optional[
            kubernetes_asyncio.client.V1alpha3PodSchedulingContextStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3PodSchedulingContextDict: ...

class V1alpha3PodSchedulingContextDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1alpha3PodSchedulingContextSpecDict
    status: kubernetes_asyncio.client.V1alpha3PodSchedulingContextStatusDict
