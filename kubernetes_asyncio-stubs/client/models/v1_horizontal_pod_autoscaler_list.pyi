import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1HorizontalPodAutoscalerList:
    api_version: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V1HorizontalPodAutoscaler]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1HorizontalPodAutoscaler],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1HorizontalPodAutoscalerListDict: ...

class V1HorizontalPodAutoscalerListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V1HorizontalPodAutoscalerDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMetaDict]
