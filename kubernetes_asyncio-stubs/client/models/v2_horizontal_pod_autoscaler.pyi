import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2HorizontalPodAutoscaler:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V2HorizontalPodAutoscalerSpec
    status: kubernetes_asyncio.client.V2HorizontalPodAutoscalerStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: typing.Optional[
            kubernetes_asyncio.client.V2HorizontalPodAutoscalerSpec
        ] = ...,
        status: typing.Optional[
            kubernetes_asyncio.client.V2HorizontalPodAutoscalerStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V2HorizontalPodAutoscalerDict: ...

class V2HorizontalPodAutoscalerDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V2HorizontalPodAutoscalerSpecDict
    status: kubernetes_asyncio.client.V2HorizontalPodAutoscalerStatusDict
