import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1DeviceSelector:
    cel: typing.Optional[kubernetes_asyncio.client.V1beta1CELDeviceSelector]

    def __init__(
        self,
        *,
        cel: typing.Optional[kubernetes_asyncio.client.V1beta1CELDeviceSelector] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1DeviceSelectorDict: ...

class V1beta1DeviceSelectorDict(typing.TypedDict, total=False):
    cel: kubernetes_asyncio.client.V1beta1CELDeviceSelectorDict
