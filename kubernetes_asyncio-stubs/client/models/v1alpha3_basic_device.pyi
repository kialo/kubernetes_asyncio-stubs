import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha3BasicDevice:
    all_nodes: typing.Optional[bool]
    attributes: typing.Optional[
        dict[str, kubernetes_asyncio.client.V1alpha3DeviceAttribute]
    ]
    capacity: typing.Optional[dict[str, str]]
    consumes_counters: typing.Optional[
        list[kubernetes_asyncio.client.V1alpha3DeviceCounterConsumption]
    ]
    node_name: typing.Optional[str]
    node_selector: typing.Optional[kubernetes_asyncio.client.V1NodeSelector]
    taints: typing.Optional[list[kubernetes_asyncio.client.V1alpha3DeviceTaint]]

    def __init__(
        self,
        *,
        all_nodes: typing.Optional[bool] = ...,
        attributes: typing.Optional[
            dict[str, kubernetes_asyncio.client.V1alpha3DeviceAttribute]
        ] = ...,
        capacity: typing.Optional[dict[str, str]] = ...,
        consumes_counters: typing.Optional[
            list[kubernetes_asyncio.client.V1alpha3DeviceCounterConsumption]
        ] = ...,
        node_name: typing.Optional[str] = ...,
        node_selector: typing.Optional[kubernetes_asyncio.client.V1NodeSelector] = ...,
        taints: typing.Optional[
            list[kubernetes_asyncio.client.V1alpha3DeviceTaint]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3BasicDeviceDict: ...

class V1alpha3BasicDeviceDict(typing.TypedDict, total=False):
    allNodes: bool
    attributes: dict[str, kubernetes_asyncio.client.V1alpha3DeviceAttributeDict]
    capacity: dict[str, str]
    consumesCounters: list[
        kubernetes_asyncio.client.V1alpha3DeviceCounterConsumptionDict
    ]
    nodeName: str
    nodeSelector: kubernetes_asyncio.client.V1NodeSelectorDict
    taints: list[kubernetes_asyncio.client.V1alpha3DeviceTaintDict]
