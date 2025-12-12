import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ServiceCIDR:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1ServiceCIDRSpec
    status: kubernetes_asyncio.client.V1ServiceCIDRStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes_asyncio.client.V1ServiceCIDRSpec] = ...,
        status: typing.Optional[kubernetes_asyncio.client.V1ServiceCIDRStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ServiceCIDRDict: ...

class V1ServiceCIDRDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1ServiceCIDRSpecDict
    status: kubernetes_asyncio.client.V1ServiceCIDRStatusDict
