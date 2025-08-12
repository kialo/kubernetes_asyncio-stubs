import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1DeviceClassConfiguration:
    opaque: typing.Optional[kubernetes_asyncio.client.V1beta1OpaqueDeviceConfiguration]

    def __init__(
        self,
        *,
        opaque: typing.Optional[
            kubernetes_asyncio.client.V1beta1OpaqueDeviceConfiguration
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1DeviceClassConfigurationDict: ...

class V1beta1DeviceClassConfigurationDict(typing.TypedDict, total=False):
    opaque: kubernetes_asyncio.client.V1beta1OpaqueDeviceConfigurationDict
