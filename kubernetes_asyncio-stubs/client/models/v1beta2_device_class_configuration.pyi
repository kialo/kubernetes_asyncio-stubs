import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2DeviceClassConfiguration:
    opaque: typing.Optional[kubernetes_asyncio.client.V1beta2OpaqueDeviceConfiguration]

    def __init__(
        self,
        *,
        opaque: typing.Optional[
            kubernetes_asyncio.client.V1beta2OpaqueDeviceConfiguration
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta2DeviceClassConfigurationDict: ...

class V1beta2DeviceClassConfigurationDict(typing.TypedDict, total=False):
    opaque: kubernetes_asyncio.client.V1beta2OpaqueDeviceConfigurationDict
