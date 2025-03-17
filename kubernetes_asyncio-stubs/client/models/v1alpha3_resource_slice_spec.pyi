import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha3ResourceSliceSpec:
    all_nodes: typing.Optional[bool]
    devices: typing.Optional[list[kubernetes_asyncio.client.V1alpha3Device]]
    driver: str
    node_name: typing.Optional[str]
    node_selector: typing.Optional[kubernetes_asyncio.client.V1NodeSelector]
    pool: kubernetes_asyncio.client.V1alpha3ResourcePool

    def __init__(
        self,
        *,
        all_nodes: typing.Optional[bool] = ...,
        devices: typing.Optional[list[kubernetes_asyncio.client.V1alpha3Device]] = ...,
        driver: str,
        node_name: typing.Optional[str] = ...,
        node_selector: typing.Optional[kubernetes_asyncio.client.V1NodeSelector] = ...,
        pool: kubernetes_asyncio.client.V1alpha3ResourcePool,
    ) -> None: ...
    def to_dict(self) -> V1alpha3ResourceSliceSpecDict: ...

class V1alpha3ResourceSliceSpecDict(typing.TypedDict, total=False):
    allNodes: bool
    devices: list[kubernetes_asyncio.client.V1alpha3DeviceDict]
    driver: str
    nodeName: str
    nodeSelector: kubernetes_asyncio.client.V1NodeSelectorDict
    pool: kubernetes_asyncio.client.V1alpha3ResourcePoolDict
