import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha2LeaseCandidateList:
    api_version: str
    items: list[kubernetes_asyncio.client.V1alpha2LeaseCandidate]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1alpha2LeaseCandidate],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2LeaseCandidateListDict: ...

class V1alpha2LeaseCandidateListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes_asyncio.client.V1alpha2LeaseCandidateDict]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMetaDict
