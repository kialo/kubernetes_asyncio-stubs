import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ContainerStatus:
    allocated_resources: typing.Optional[dict[str, str]]
    container_id: typing.Optional[str]
    image: str
    image_id: str
    last_state: typing.Optional[kubernetes_asyncio.client.V1ContainerState]
    name: str
    ready: bool
    resources: typing.Optional[kubernetes_asyncio.client.V1ResourceRequirements]
    restart_count: int
    started: typing.Optional[bool]
    state: typing.Optional[kubernetes_asyncio.client.V1ContainerState]

    def __init__(
        self,
        *,
        allocated_resources: typing.Optional[dict[str, str]] = ...,
        container_id: typing.Optional[str] = ...,
        image: str,
        image_id: str,
        last_state: typing.Optional[kubernetes_asyncio.client.V1ContainerState] = ...,
        name: str,
        ready: bool,
        resources: typing.Optional[
            kubernetes_asyncio.client.V1ResourceRequirements
        ] = ...,
        restart_count: int,
        started: typing.Optional[bool] = ...,
        state: typing.Optional[kubernetes_asyncio.client.V1ContainerState] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ContainerStatusDict: ...

class V1ContainerStatusDict(typing.TypedDict, total=False):
    allocatedResources: typing.Optional[dict[str, str]]
    containerID: typing.Optional[str]
    image: str
    imageID: str
    lastState: typing.Optional[kubernetes_asyncio.client.V1ContainerStateDict]
    name: str
    ready: bool
    resources: typing.Optional[kubernetes_asyncio.client.V1ResourceRequirementsDict]
    restartCount: int
    started: typing.Optional[bool]
    state: typing.Optional[kubernetes_asyncio.client.V1ContainerStateDict]
