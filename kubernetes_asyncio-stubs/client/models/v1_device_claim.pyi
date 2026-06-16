import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1DeviceClaim:
    config: typing.Optional[list[kubernetes_asyncio.client.V1DeviceClaimConfiguration]]
    constraints: typing.Optional[list[kubernetes_asyncio.client.V1DeviceConstraint]]
    requests: typing.Optional[list[kubernetes_asyncio.client.V1DeviceRequest]]

    def __init__(
        self,
        *,
        config: typing.Optional[
            list[kubernetes_asyncio.client.V1DeviceClaimConfiguration]
        ] = ...,
        constraints: typing.Optional[
            list[kubernetes_asyncio.client.V1DeviceConstraint]
        ] = ...,
        requests: typing.Optional[
            list[kubernetes_asyncio.client.V1DeviceRequest]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1DeviceClaimDict: ...

class V1DeviceClaimDict(typing.TypedDict, total=False):
    config: list[kubernetes_asyncio.client.V1DeviceClaimConfigurationDict]
    constraints: list[kubernetes_asyncio.client.V1DeviceConstraintDict]
    requests: list[kubernetes_asyncio.client.V1DeviceRequestDict]
