import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1Deployment:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1DeploymentSpec
    status: kubernetes_asyncio.client.V1DeploymentStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes_asyncio.client.V1DeploymentSpec] = ...,
        status: typing.Optional[kubernetes_asyncio.client.V1DeploymentStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1DeploymentDict: ...

class V1DeploymentDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1DeploymentSpecDict
    status: kubernetes_asyncio.client.V1DeploymentStatusDict
