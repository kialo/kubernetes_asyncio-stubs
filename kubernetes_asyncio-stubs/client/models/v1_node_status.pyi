import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NodeStatus:
    addresses: typing.Optional[list[kubernetes_asyncio.client.V1NodeAddress]]
    allocatable: typing.Optional[dict[str, str]]
    capacity: typing.Optional[dict[str, str]]
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1NodeCondition]]
    config: typing.Optional[kubernetes_asyncio.client.V1NodeConfigStatus]
    daemon_endpoints: typing.Optional[kubernetes_asyncio.client.V1NodeDaemonEndpoints]
    images: typing.Optional[list[kubernetes_asyncio.client.V1ContainerImage]]
    node_info: typing.Optional[kubernetes_asyncio.client.V1NodeSystemInfo]
    phase: typing.Optional[str]
    runtime_handlers: typing.Optional[
        list[kubernetes_asyncio.client.V1NodeRuntimeHandler]
    ]
    volumes_attached: typing.Optional[list[kubernetes_asyncio.client.V1AttachedVolume]]
    volumes_in_use: typing.Optional[list[str]]

    def __init__(
        self,
        *,
        addresses: typing.Optional[list[kubernetes_asyncio.client.V1NodeAddress]] = ...,
        allocatable: typing.Optional[dict[str, str]] = ...,
        capacity: typing.Optional[dict[str, str]] = ...,
        conditions: typing.Optional[
            list[kubernetes_asyncio.client.V1NodeCondition]
        ] = ...,
        config: typing.Optional[kubernetes_asyncio.client.V1NodeConfigStatus] = ...,
        daemon_endpoints: typing.Optional[
            kubernetes_asyncio.client.V1NodeDaemonEndpoints
        ] = ...,
        images: typing.Optional[list[kubernetes_asyncio.client.V1ContainerImage]] = ...,
        node_info: typing.Optional[kubernetes_asyncio.client.V1NodeSystemInfo] = ...,
        phase: typing.Optional[str] = ...,
        runtime_handlers: typing.Optional[
            list[kubernetes_asyncio.client.V1NodeRuntimeHandler]
        ] = ...,
        volumes_attached: typing.Optional[
            list[kubernetes_asyncio.client.V1AttachedVolume]
        ] = ...,
        volumes_in_use: typing.Optional[list[str]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1NodeStatusDict: ...

class V1NodeStatusDict(typing.TypedDict, total=False):
    addresses: list[kubernetes_asyncio.client.V1NodeAddressDict]
    allocatable: dict[str, str]
    capacity: dict[str, str]
    conditions: list[kubernetes_asyncio.client.V1NodeConditionDict]
    config: kubernetes_asyncio.client.V1NodeConfigStatusDict
    daemonEndpoints: kubernetes_asyncio.client.V1NodeDaemonEndpointsDict
    images: list[kubernetes_asyncio.client.V1ContainerImageDict]
    nodeInfo: kubernetes_asyncio.client.V1NodeSystemInfoDict
    phase: str
    runtimeHandlers: list[kubernetes_asyncio.client.V1NodeRuntimeHandlerDict]
    volumesAttached: list[kubernetes_asyncio.client.V1AttachedVolumeDict]
    volumesInUse: list[str]
