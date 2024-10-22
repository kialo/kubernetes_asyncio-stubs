import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NodeRuntimeHandler:
    features: typing.Optional[kubernetes_asyncio.client.V1NodeRuntimeHandlerFeatures]
    name: typing.Optional[str]

    def __init__(
        self,
        *,
        features: typing.Optional[
            kubernetes_asyncio.client.V1NodeRuntimeHandlerFeatures
        ] = ...,
        name: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1NodeRuntimeHandlerDict: ...

class V1NodeRuntimeHandlerDict(typing.TypedDict, total=False):
    features: kubernetes_asyncio.client.V1NodeRuntimeHandlerFeaturesDict
    name: str