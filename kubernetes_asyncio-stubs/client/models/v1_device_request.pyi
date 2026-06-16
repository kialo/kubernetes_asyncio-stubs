import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1DeviceRequest:
    exactly: typing.Optional[kubernetes_asyncio.client.V1ExactDeviceRequest]
    first_available: typing.Optional[list[kubernetes_asyncio.client.V1DeviceSubRequest]]
    name: str

    def __init__(
        self,
        *,
        exactly: typing.Optional[kubernetes_asyncio.client.V1ExactDeviceRequest] = ...,
        first_available: typing.Optional[
            list[kubernetes_asyncio.client.V1DeviceSubRequest]
        ] = ...,
        name: str,
    ) -> None: ...
    def to_dict(self) -> V1DeviceRequestDict: ...

class V1DeviceRequestDict(typing.TypedDict, total=False):
    exactly: kubernetes_asyncio.client.V1ExactDeviceRequestDict
    firstAvailable: list[kubernetes_asyncio.client.V1DeviceSubRequestDict]
    name: str
