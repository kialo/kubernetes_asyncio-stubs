import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha3DeviceSelector:
    cel: typing.Optional[kubernetes_asyncio.client.V1alpha3CELDeviceSelector]

    def __init__(
        self,
        *,
        cel: typing.Optional[kubernetes_asyncio.client.V1alpha3CELDeviceSelector] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3DeviceSelectorDict: ...

class V1alpha3DeviceSelectorDict(typing.TypedDict, total=False):
    cel: kubernetes_asyncio.client.V1alpha3CELDeviceSelectorDict
