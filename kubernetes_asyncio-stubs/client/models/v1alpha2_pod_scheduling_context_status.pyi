import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha2PodSchedulingContextStatus:
    resource_claims: typing.Optional[
        list[kubernetes_asyncio.client.V1alpha2ResourceClaimSchedulingStatus]
    ]

    def __init__(
        self,
        *,
        resource_claims: typing.Optional[
            list[kubernetes_asyncio.client.V1alpha2ResourceClaimSchedulingStatus]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2PodSchedulingContextStatusDict: ...

class V1alpha2PodSchedulingContextStatusDict(typing.TypedDict, total=False):
    resourceClaims: list[
        kubernetes_asyncio.client.V1alpha2ResourceClaimSchedulingStatusDict
    ]