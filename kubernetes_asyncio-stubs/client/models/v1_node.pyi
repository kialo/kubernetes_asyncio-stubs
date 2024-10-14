import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1Node:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1NodeSpec
    status: kubernetes_asyncio.client.V1NodeStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes_asyncio.client.V1NodeSpec] = ...,
        status: typing.Optional[kubernetes_asyncio.client.V1NodeStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1NodeDict: ...

class V1NodeDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1NodeSpecDict
    status: kubernetes_asyncio.client.V1NodeStatusDict
