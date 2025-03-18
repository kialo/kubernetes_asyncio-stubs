import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha3ResourceClaim:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1alpha3ResourceClaimSpec
    status: kubernetes_asyncio.client.V1alpha3ResourceClaimStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: kubernetes_asyncio.client.V1alpha3ResourceClaimSpec,
        status: typing.Optional[
            kubernetes_asyncio.client.V1alpha3ResourceClaimStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3ResourceClaimDict: ...

class V1alpha3ResourceClaimDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1alpha3ResourceClaimSpecDict
    status: kubernetes_asyncio.client.V1alpha3ResourceClaimStatusDict
