import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1LeaseCandidate:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1beta1LeaseCandidateSpec

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: typing.Optional[
            kubernetes_asyncio.client.V1beta1LeaseCandidateSpec
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1LeaseCandidateDict: ...

class V1beta1LeaseCandidateDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1beta1LeaseCandidateSpecDict
