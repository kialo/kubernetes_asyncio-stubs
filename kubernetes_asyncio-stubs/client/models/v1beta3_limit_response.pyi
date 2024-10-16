import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta3LimitResponse:
    queuing: typing.Optional[kubernetes_asyncio.client.V1beta3QueuingConfiguration]
    type: str

    def __init__(
        self,
        *,
        queuing: typing.Optional[
            kubernetes_asyncio.client.V1beta3QueuingConfiguration
        ] = ...,
        type: str,
    ) -> None: ...
    def to_dict(self) -> V1beta3LimitResponseDict: ...

class V1beta3LimitResponseDict(typing.TypedDict, total=False):
    queuing: kubernetes_asyncio.client.V1beta3QueuingConfigurationDict
    type: str
