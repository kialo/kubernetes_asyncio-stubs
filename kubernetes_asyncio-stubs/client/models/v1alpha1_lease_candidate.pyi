import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1LeaseCandidate:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1alpha1LeaseCandidateSpec

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: typing.Optional[
            kubernetes_asyncio.client.V1alpha1LeaseCandidateSpec
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1LeaseCandidateDict: ...

class V1alpha1LeaseCandidateDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1alpha1LeaseCandidateSpecDict
