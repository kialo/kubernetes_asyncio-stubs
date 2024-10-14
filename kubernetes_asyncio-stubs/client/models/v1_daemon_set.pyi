import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1DaemonSet:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1DaemonSetSpec
    status: kubernetes_asyncio.client.V1DaemonSetStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes_asyncio.client.V1DaemonSetSpec] = ...,
        status: typing.Optional[kubernetes_asyncio.client.V1DaemonSetStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1DaemonSetDict: ...

class V1DaemonSetDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1DaemonSetSpecDict
    status: kubernetes_asyncio.client.V1DaemonSetStatusDict
