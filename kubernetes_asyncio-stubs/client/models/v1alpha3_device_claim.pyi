import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha3DeviceClaim:
    config: typing.Optional[
        list[kubernetes_asyncio.client.V1alpha3DeviceClaimConfiguration]
    ]
    constraints: typing.Optional[
        list[kubernetes_asyncio.client.V1alpha3DeviceConstraint]
    ]
    requests: typing.Optional[list[kubernetes_asyncio.client.V1alpha3DeviceRequest]]

    def __init__(
        self,
        *,
        config: typing.Optional[
            list[kubernetes_asyncio.client.V1alpha3DeviceClaimConfiguration]
        ] = ...,
        constraints: typing.Optional[
            list[kubernetes_asyncio.client.V1alpha3DeviceConstraint]
        ] = ...,
        requests: typing.Optional[
            list[kubernetes_asyncio.client.V1alpha3DeviceRequest]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3DeviceClaimDict: ...

class V1alpha3DeviceClaimDict(typing.TypedDict, total=False):
    config: list[kubernetes_asyncio.client.V1alpha3DeviceClaimConfigurationDict]
    constraints: list[kubernetes_asyncio.client.V1alpha3DeviceConstraintDict]
    requests: list[kubernetes_asyncio.client.V1alpha3DeviceRequestDict]
