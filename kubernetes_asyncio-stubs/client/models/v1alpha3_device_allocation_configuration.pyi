import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha3DeviceAllocationConfiguration:
    opaque: typing.Optional[kubernetes_asyncio.client.V1alpha3OpaqueDeviceConfiguration]
    requests: typing.Optional[list[str]]
    source: str

    def __init__(
        self,
        *,
        opaque: typing.Optional[
            kubernetes_asyncio.client.V1alpha3OpaqueDeviceConfiguration
        ] = ...,
        requests: typing.Optional[list[str]] = ...,
        source: str,
    ) -> None: ...
    def to_dict(self) -> V1alpha3DeviceAllocationConfigurationDict: ...

class V1alpha3DeviceAllocationConfigurationDict(typing.TypedDict, total=False):
    opaque: kubernetes_asyncio.client.V1alpha3OpaqueDeviceConfigurationDict
    requests: list[str]
    source: str
