import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha3ResourceClaimList:
    api_version: str
    items: list[kubernetes_asyncio.client.V1alpha3ResourceClaim]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1alpha3ResourceClaim],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3ResourceClaimListDict: ...

class V1alpha3ResourceClaimListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes_asyncio.client.V1alpha3ResourceClaimDict]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMetaDict
