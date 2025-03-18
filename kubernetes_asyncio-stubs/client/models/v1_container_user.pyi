import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ContainerUser:
    linux: typing.Optional[kubernetes_asyncio.client.V1LinuxContainerUser]

    def __init__(
        self,
        *,
        linux: typing.Optional[kubernetes_asyncio.client.V1LinuxContainerUser] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ContainerUserDict: ...

class V1ContainerUserDict(typing.TypedDict, total=False):
    linux: kubernetes_asyncio.client.V1LinuxContainerUserDict
