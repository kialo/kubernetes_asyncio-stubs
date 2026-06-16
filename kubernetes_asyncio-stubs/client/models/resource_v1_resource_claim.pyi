import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class ResourceV1ResourceClaim:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1ResourceClaimSpec
    status: kubernetes_asyncio.client.V1ResourceClaimStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: kubernetes_asyncio.client.V1ResourceClaimSpec,
        status: typing.Optional[kubernetes_asyncio.client.V1ResourceClaimStatus] = ...,
    ) -> None: ...
    def to_dict(self) -> ResourceV1ResourceClaimDict: ...

class ResourceV1ResourceClaimDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1ResourceClaimSpecDict
    status: kubernetes_asyncio.client.V1ResourceClaimStatusDict
