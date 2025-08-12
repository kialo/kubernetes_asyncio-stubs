import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1DeviceClaimConfiguration:
    opaque: typing.Optional[kubernetes_asyncio.client.V1beta1OpaqueDeviceConfiguration]
    requests: typing.Optional[list[str]]

    def __init__(
        self,
        *,
        opaque: typing.Optional[
            kubernetes_asyncio.client.V1beta1OpaqueDeviceConfiguration
        ] = ...,
        requests: typing.Optional[list[str]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1DeviceClaimConfigurationDict: ...

class V1beta1DeviceClaimConfigurationDict(typing.TypedDict, total=False):
    opaque: kubernetes_asyncio.client.V1beta1OpaqueDeviceConfigurationDict
    requests: list[str]
