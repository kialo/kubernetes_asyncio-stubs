import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1ResourceSliceSpec:
    all_nodes: typing.Optional[bool]
    devices: typing.Optional[list[kubernetes_asyncio.client.V1beta1Device]]
    driver: str
    node_name: typing.Optional[str]
    node_selector: typing.Optional[kubernetes_asyncio.client.V1NodeSelector]
    pool: kubernetes_asyncio.client.V1beta1ResourcePool

    def __init__(
        self,
        *,
        all_nodes: typing.Optional[bool] = ...,
        devices: typing.Optional[list[kubernetes_asyncio.client.V1beta1Device]] = ...,
        driver: str,
        node_name: typing.Optional[str] = ...,
        node_selector: typing.Optional[kubernetes_asyncio.client.V1NodeSelector] = ...,
        pool: kubernetes_asyncio.client.V1beta1ResourcePool,
    ) -> None: ...
    def to_dict(self) -> V1beta1ResourceSliceSpecDict: ...

class V1beta1ResourceSliceSpecDict(typing.TypedDict, total=False):
    allNodes: bool
    devices: list[kubernetes_asyncio.client.V1beta1DeviceDict]
    driver: str
    nodeName: str
    nodeSelector: kubernetes_asyncio.client.V1NodeSelectorDict
    pool: kubernetes_asyncio.client.V1beta1ResourcePoolDict
