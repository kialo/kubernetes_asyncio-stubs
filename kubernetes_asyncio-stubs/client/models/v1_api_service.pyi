import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1APIService:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1APIServiceSpec
    status: kubernetes_asyncio.client.V1APIServiceStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes_asyncio.client.V1APIServiceSpec] = ...,
        status: typing.Optional[kubernetes_asyncio.client.V1APIServiceStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> V1APIServiceDict: ...

class V1APIServiceDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1APIServiceSpecDict
    status: kubernetes_asyncio.client.V1APIServiceStatusDict
