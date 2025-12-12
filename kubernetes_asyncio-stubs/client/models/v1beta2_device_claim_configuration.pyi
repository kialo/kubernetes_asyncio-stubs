import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2DeviceClaimConfiguration:
    opaque: typing.Optional[kubernetes_asyncio.client.V1beta2OpaqueDeviceConfiguration]
    requests: typing.Optional[list[str]]

    def __init__(
        self,
        *,
        opaque: typing.Optional[
            kubernetes_asyncio.client.V1beta2OpaqueDeviceConfiguration
        ] = ...,
        requests: typing.Optional[list[str]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta2DeviceClaimConfigurationDict: ...

class V1beta2DeviceClaimConfigurationDict(typing.TypedDict, total=False):
    opaque: kubernetes_asyncio.client.V1beta2OpaqueDeviceConfigurationDict
    requests: list[str]
