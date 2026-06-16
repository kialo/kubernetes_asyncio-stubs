import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ResourceClaimSpec:
    devices: typing.Optional[kubernetes_asyncio.client.V1DeviceClaim]

    def __init__(
        self, *, devices: typing.Optional[kubernetes_asyncio.client.V1DeviceClaim] = ...
    ) -> None: ...
    def to_dict(self) -> V1ResourceClaimSpecDict: ...

class V1ResourceClaimSpecDict(typing.TypedDict, total=False):
    devices: kubernetes_asyncio.client.V1DeviceClaimDict
