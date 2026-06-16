import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1DeviceSelector:
    cel: typing.Optional[kubernetes_asyncio.client.V1CELDeviceSelector]

    def __init__(
        self,
        *,
        cel: typing.Optional[kubernetes_asyncio.client.V1CELDeviceSelector] = ...,
    ) -> None: ...
    def to_dict(self) -> V1DeviceSelectorDict: ...

class V1DeviceSelectorDict(typing.TypedDict, total=False):
    cel: kubernetes_asyncio.client.V1CELDeviceSelectorDict
