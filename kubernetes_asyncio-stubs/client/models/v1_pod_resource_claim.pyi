import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PodResourceClaim:
    name: str
    source: typing.Optional[kubernetes_asyncio.client.V1ClaimSource]

    def __init__(
        self,
        *,
        name: str,
        source: typing.Optional[kubernetes_asyncio.client.V1ClaimSource] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PodResourceClaimDict: ...

class V1PodResourceClaimDict(typing.TypedDict, total=False):
    name: str
    source: typing.Optional[kubernetes_asyncio.client.V1ClaimSourceDict]
