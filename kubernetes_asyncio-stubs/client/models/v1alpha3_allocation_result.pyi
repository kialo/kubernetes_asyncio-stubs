import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha3AllocationResult:
    devices: typing.Optional[kubernetes_asyncio.client.V1alpha3DeviceAllocationResult]
    node_selector: typing.Optional[kubernetes_asyncio.client.V1NodeSelector]

    def __init__(
        self,
        *,
        devices: typing.Optional[
            kubernetes_asyncio.client.V1alpha3DeviceAllocationResult
        ] = ...,
        node_selector: typing.Optional[kubernetes_asyncio.client.V1NodeSelector] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3AllocationResultDict: ...

class V1alpha3AllocationResultDict(typing.TypedDict, total=False):
    devices: kubernetes_asyncio.client.V1alpha3DeviceAllocationResultDict
    nodeSelector: kubernetes_asyncio.client.V1NodeSelectorDict
