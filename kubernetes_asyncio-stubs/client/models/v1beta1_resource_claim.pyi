import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1ResourceClaim:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1beta1ResourceClaimSpec
    status: kubernetes_asyncio.client.V1beta1ResourceClaimStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: kubernetes_asyncio.client.V1beta1ResourceClaimSpec,
        status: typing.Optional[
            kubernetes_asyncio.client.V1beta1ResourceClaimStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1ResourceClaimDict: ...

class V1beta1ResourceClaimDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1beta1ResourceClaimSpecDict
    status: kubernetes_asyncio.client.V1beta1ResourceClaimStatusDict
