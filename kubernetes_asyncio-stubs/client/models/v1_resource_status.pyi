import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ResourceStatus:
    name: str
    resources: typing.Optional[list[kubernetes_asyncio.client.V1ResourceHealth]]

    def __init__(
        self,
        *,
        name: str,
        resources: typing.Optional[
            list[kubernetes_asyncio.client.V1ResourceHealth]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ResourceStatusDict: ...

class V1ResourceStatusDict(typing.TypedDict, total=False):
    name: str
    resources: list[kubernetes_asyncio.client.V1ResourceHealthDict]
