import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha3ResourceClaimTemplate:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1alpha3ResourceClaimTemplateSpec

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: kubernetes_asyncio.client.V1alpha3ResourceClaimTemplateSpec,
    ) -> None: ...
    def to_dict(self) -> V1alpha3ResourceClaimTemplateDict: ...

class V1alpha3ResourceClaimTemplateDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1alpha3ResourceClaimTemplateSpecDict
