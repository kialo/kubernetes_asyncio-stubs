import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1ResourceClaimTemplateSpec:
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: kubernetes_asyncio.client.V1beta1ResourceClaimSpec

    def __init__(
        self,
        *,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: kubernetes_asyncio.client.V1beta1ResourceClaimSpec,
    ) -> None: ...
    def to_dict(self) -> V1beta1ResourceClaimTemplateSpecDict: ...

class V1beta1ResourceClaimTemplateSpecDict(typing.TypedDict, total=False):
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1beta1ResourceClaimSpecDict
