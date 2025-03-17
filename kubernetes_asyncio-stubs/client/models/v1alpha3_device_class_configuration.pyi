import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha3DeviceClassConfiguration:
    opaque: typing.Optional[kubernetes_asyncio.client.V1alpha3OpaqueDeviceConfiguration]

    def __init__(
        self,
        *,
        opaque: typing.Optional[
            kubernetes_asyncio.client.V1alpha3OpaqueDeviceConfiguration
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3DeviceClassConfigurationDict: ...

class V1alpha3DeviceClassConfigurationDict(typing.TypedDict, total=False):
    opaque: kubernetes_asyncio.client.V1alpha3OpaqueDeviceConfigurationDict
