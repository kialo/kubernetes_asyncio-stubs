import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ResourceClaimStatus:
    allocation: typing.Optional[kubernetes_asyncio.client.V1AllocationResult]
    devices: typing.Optional[list[kubernetes_asyncio.client.V1AllocatedDeviceStatus]]
    reserved_for: typing.Optional[
        list[kubernetes_asyncio.client.V1ResourceClaimConsumerReference]
    ]

    def __init__(
        self,
        *,
        allocation: typing.Optional[kubernetes_asyncio.client.V1AllocationResult] = ...,
        devices: typing.Optional[
            list[kubernetes_asyncio.client.V1AllocatedDeviceStatus]
        ] = ...,
        reserved_for: typing.Optional[
            list[kubernetes_asyncio.client.V1ResourceClaimConsumerReference]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ResourceClaimStatusDict: ...

class V1ResourceClaimStatusDict(typing.TypedDict, total=False):
    allocation: kubernetes_asyncio.client.V1AllocationResultDict
    devices: list[kubernetes_asyncio.client.V1AllocatedDeviceStatusDict]
    reservedFor: list[kubernetes_asyncio.client.V1ResourceClaimConsumerReferenceDict]
