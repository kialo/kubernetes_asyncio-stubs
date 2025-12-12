import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2ResourceClaimTemplateSpec:
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: kubernetes_asyncio.client.V1beta2ResourceClaimSpec

    def __init__(
        self,
        *,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: kubernetes_asyncio.client.V1beta2ResourceClaimSpec,
    ) -> None: ...
    def to_dict(self) -> V1beta2ResourceClaimTemplateSpecDict: ...

class V1beta2ResourceClaimTemplateSpecDict(typing.TypedDict, total=False):
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1beta2ResourceClaimSpecDict
