import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ResourceClaimList:
    api_version: str
    items: list[kubernetes_asyncio.client.ResourceV1ResourceClaim]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.ResourceV1ResourceClaim],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ResourceClaimListDict: ...

class V1ResourceClaimListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes_asyncio.client.ResourceV1ResourceClaimDict]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMetaDict
