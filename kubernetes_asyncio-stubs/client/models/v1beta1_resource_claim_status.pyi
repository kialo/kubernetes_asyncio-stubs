import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1ResourceClaimStatus:
    allocation: typing.Optional[kubernetes_asyncio.client.V1beta1AllocationResult]
    devices: typing.Optional[
        list[kubernetes_asyncio.client.V1beta1AllocatedDeviceStatus]
    ]
    reserved_for: typing.Optional[
        list[kubernetes_asyncio.client.V1beta1ResourceClaimConsumerReference]
    ]

    def __init__(
        self,
        *,
        allocation: typing.Optional[
            kubernetes_asyncio.client.V1beta1AllocationResult
        ] = ...,
        devices: typing.Optional[
            list[kubernetes_asyncio.client.V1beta1AllocatedDeviceStatus]
        ] = ...,
        reserved_for: typing.Optional[
            list[kubernetes_asyncio.client.V1beta1ResourceClaimConsumerReference]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1ResourceClaimStatusDict: ...

class V1beta1ResourceClaimStatusDict(typing.TypedDict, total=False):
    allocation: kubernetes_asyncio.client.V1beta1AllocationResultDict
    devices: list[kubernetes_asyncio.client.V1beta1AllocatedDeviceStatusDict]
    reservedFor: list[
        kubernetes_asyncio.client.V1beta1ResourceClaimConsumerReferenceDict
    ]
