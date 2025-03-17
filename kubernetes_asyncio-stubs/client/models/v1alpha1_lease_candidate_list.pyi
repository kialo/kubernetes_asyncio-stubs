import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1LeaseCandidateList:
    api_version: str
    items: list[kubernetes_asyncio.client.V1alpha1LeaseCandidate]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1alpha1LeaseCandidate],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1LeaseCandidateListDict: ...

class V1alpha1LeaseCandidateListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes_asyncio.client.V1alpha1LeaseCandidateDict]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMetaDict
