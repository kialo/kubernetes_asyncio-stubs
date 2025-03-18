import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha3Device:
    basic: typing.Optional[kubernetes_asyncio.client.V1alpha3BasicDevice]
    name: str

    def __init__(
        self,
        *,
        basic: typing.Optional[kubernetes_asyncio.client.V1alpha3BasicDevice] = ...,
        name: str,
    ) -> None: ...
    def to_dict(self) -> V1alpha3DeviceDict: ...

class V1alpha3DeviceDict(typing.TypedDict, total=False):
    basic: kubernetes_asyncio.client.V1alpha3BasicDeviceDict
    name: str
