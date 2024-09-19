import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta3PriorityLevelConfigurationSpec:
    exempt: typing.Optional[
        kubernetes_asyncio.client.V1beta3ExemptPriorityLevelConfiguration
    ]
    limited: typing.Optional[
        kubernetes_asyncio.client.V1beta3LimitedPriorityLevelConfiguration
    ]
    type: str

    def __init__(
        self,
        *,
        exempt: typing.Optional[
            kubernetes_asyncio.client.V1beta3ExemptPriorityLevelConfiguration
        ] = ...,
        limited: typing.Optional[
            kubernetes_asyncio.client.V1beta3LimitedPriorityLevelConfiguration
        ] = ...,
        type: str,
    ) -> None: ...
    def to_dict(self) -> V1beta3PriorityLevelConfigurationSpecDict: ...

class V1beta3PriorityLevelConfigurationSpecDict(typing.TypedDict, total=False):
    exempt: typing.Optional[
        kubernetes_asyncio.client.V1beta3ExemptPriorityLevelConfigurationDict
    ]
    limited: typing.Optional[
        kubernetes_asyncio.client.V1beta3LimitedPriorityLevelConfigurationDict
    ]
    type: str
