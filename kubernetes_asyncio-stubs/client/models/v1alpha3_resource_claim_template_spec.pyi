import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha3ResourceClaimTemplateSpec:
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: kubernetes_asyncio.client.V1alpha3ResourceClaimSpec

    def __init__(
        self,
        *,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: kubernetes_asyncio.client.V1alpha3ResourceClaimSpec,
    ) -> None: ...
    def to_dict(self) -> V1alpha3ResourceClaimTemplateSpecDict: ...

class V1alpha3ResourceClaimTemplateSpecDict(typing.TypedDict, total=False):
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1alpha3ResourceClaimSpecDict
