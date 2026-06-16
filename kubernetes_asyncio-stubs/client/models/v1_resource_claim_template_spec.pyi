import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ResourceClaimTemplateSpec:
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: kubernetes_asyncio.client.V1ResourceClaimSpec

    def __init__(
        self,
        *,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: kubernetes_asyncio.client.V1ResourceClaimSpec,
    ) -> None: ...
    def to_dict(self) -> V1ResourceClaimTemplateSpecDict: ...

class V1ResourceClaimTemplateSpecDict(typing.TypedDict, total=False):
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1ResourceClaimSpecDict
