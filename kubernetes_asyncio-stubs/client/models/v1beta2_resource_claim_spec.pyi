import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2ResourceClaimSpec:
    devices: typing.Optional[kubernetes_asyncio.client.V1beta2DeviceClaim]

    def __init__(
        self,
        *,
        devices: typing.Optional[kubernetes_asyncio.client.V1beta2DeviceClaim] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta2ResourceClaimSpecDict: ...

class V1beta2ResourceClaimSpecDict(typing.TypedDict, total=False):
    devices: kubernetes_asyncio.client.V1beta2DeviceClaimDict
