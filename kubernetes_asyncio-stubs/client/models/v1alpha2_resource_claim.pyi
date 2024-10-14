import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha2ResourceClaim:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1alpha2ResourceClaimSpec
    status: kubernetes_asyncio.client.V1alpha2ResourceClaimStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: kubernetes_asyncio.client.V1alpha2ResourceClaimSpec,
        status: typing.Optional[
            kubernetes_asyncio.client.V1alpha2ResourceClaimStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2ResourceClaimDict: ...

class V1alpha2ResourceClaimDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1alpha2ResourceClaimSpecDict
    status: kubernetes_asyncio.client.V1alpha2ResourceClaimStatusDict
