import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2AllocationResult:
    devices: typing.Optional[kubernetes_asyncio.client.V1beta2DeviceAllocationResult]
    node_selector: typing.Optional[kubernetes_asyncio.client.V1NodeSelector]

    def __init__(
        self,
        *,
        devices: typing.Optional[
            kubernetes_asyncio.client.V1beta2DeviceAllocationResult
        ] = ...,
        node_selector: typing.Optional[kubernetes_asyncio.client.V1NodeSelector] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta2AllocationResultDict: ...

class V1beta2AllocationResultDict(typing.TypedDict, total=False):
    devices: kubernetes_asyncio.client.V1beta2DeviceAllocationResultDict
    nodeSelector: kubernetes_asyncio.client.V1NodeSelectorDict
