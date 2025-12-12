import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2ResourceClaimTemplate:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1beta2ResourceClaimTemplateSpec

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: kubernetes_asyncio.client.V1beta2ResourceClaimTemplateSpec,
    ) -> None: ...
    def to_dict(self) -> V1beta2ResourceClaimTemplateDict: ...

class V1beta2ResourceClaimTemplateDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1beta2ResourceClaimTemplateSpecDict
