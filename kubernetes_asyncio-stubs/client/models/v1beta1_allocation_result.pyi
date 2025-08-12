import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1AllocationResult:
    devices: typing.Optional[kubernetes_asyncio.client.V1beta1DeviceAllocationResult]
    node_selector: typing.Optional[kubernetes_asyncio.client.V1NodeSelector]

    def __init__(
        self,
        *,
        devices: typing.Optional[
            kubernetes_asyncio.client.V1beta1DeviceAllocationResult
        ] = ...,
        node_selector: typing.Optional[kubernetes_asyncio.client.V1NodeSelector] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1AllocationResultDict: ...

class V1beta1AllocationResultDict(typing.TypedDict, total=False):
    devices: kubernetes_asyncio.client.V1beta1DeviceAllocationResultDict
    nodeSelector: kubernetes_asyncio.client.V1NodeSelectorDict
