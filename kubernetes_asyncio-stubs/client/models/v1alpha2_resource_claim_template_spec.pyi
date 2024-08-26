import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha2ResourceClaimTemplateSpec:
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: kubernetes_asyncio.client.V1alpha2ResourceClaimSpec

    def __init__(
        self,
        *,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: kubernetes_asyncio.client.V1alpha2ResourceClaimSpec,
    ) -> None: ...
    def to_dict(self) -> V1alpha2ResourceClaimTemplateSpecDict: ...

class V1alpha2ResourceClaimTemplateSpecDict(typing.TypedDict, total=False):
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: kubernetes_asyncio.client.V1alpha2ResourceClaimSpecDict
