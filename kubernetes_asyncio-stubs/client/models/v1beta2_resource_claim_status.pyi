import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2ResourceClaimStatus:
    allocation: typing.Optional[kubernetes_asyncio.client.V1beta2AllocationResult]
    devices: typing.Optional[
        list[kubernetes_asyncio.client.V1beta2AllocatedDeviceStatus]
    ]
    reserved_for: typing.Optional[
        list[kubernetes_asyncio.client.V1beta2ResourceClaimConsumerReference]
    ]

    def __init__(
        self,
        *,
        allocation: typing.Optional[
            kubernetes_asyncio.client.V1beta2AllocationResult
        ] = ...,
        devices: typing.Optional[
            list[kubernetes_asyncio.client.V1beta2AllocatedDeviceStatus]
        ] = ...,
        reserved_for: typing.Optional[
            list[kubernetes_asyncio.client.V1beta2ResourceClaimConsumerReference]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta2ResourceClaimStatusDict: ...

class V1beta2ResourceClaimStatusDict(typing.TypedDict, total=False):
    allocation: kubernetes_asyncio.client.V1beta2AllocationResultDict
    devices: list[kubernetes_asyncio.client.V1beta2AllocatedDeviceStatusDict]
    reservedFor: list[
        kubernetes_asyncio.client.V1beta2ResourceClaimConsumerReferenceDict
    ]
