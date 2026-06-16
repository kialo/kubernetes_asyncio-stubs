import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ResourceSliceSpec:
    all_nodes: typing.Optional[bool]
    devices: typing.Optional[list[kubernetes_asyncio.client.V1Device]]
    driver: str
    node_name: typing.Optional[str]
    node_selector: typing.Optional[kubernetes_asyncio.client.V1NodeSelector]
    per_device_node_selection: typing.Optional[bool]
    pool: kubernetes_asyncio.client.V1ResourcePool
    shared_counters: typing.Optional[list[kubernetes_asyncio.client.V1CounterSet]]

    def __init__(
        self,
        *,
        all_nodes: typing.Optional[bool] = ...,
        devices: typing.Optional[list[kubernetes_asyncio.client.V1Device]] = ...,
        driver: str,
        node_name: typing.Optional[str] = ...,
        node_selector: typing.Optional[kubernetes_asyncio.client.V1NodeSelector] = ...,
        per_device_node_selection: typing.Optional[bool] = ...,
        pool: kubernetes_asyncio.client.V1ResourcePool,
        shared_counters: typing.Optional[
            list[kubernetes_asyncio.client.V1CounterSet]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ResourceSliceSpecDict: ...

class V1ResourceSliceSpecDict(typing.TypedDict, total=False):
    allNodes: bool
    devices: list[kubernetes_asyncio.client.V1DeviceDict]
    driver: str
    nodeName: str
    nodeSelector: kubernetes_asyncio.client.V1NodeSelectorDict
    perDeviceNodeSelection: bool
    pool: kubernetes_asyncio.client.V1ResourcePoolDict
    sharedCounters: list[kubernetes_asyncio.client.V1CounterSetDict]
