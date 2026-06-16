import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1DeviceClassConfiguration:
    opaque: typing.Optional[kubernetes_asyncio.client.V1OpaqueDeviceConfiguration]

    def __init__(
        self,
        *,
        opaque: typing.Optional[
            kubernetes_asyncio.client.V1OpaqueDeviceConfiguration
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1DeviceClassConfigurationDict: ...

class V1DeviceClassConfigurationDict(typing.TypedDict, total=False):
    opaque: kubernetes_asyncio.client.V1OpaqueDeviceConfigurationDict
