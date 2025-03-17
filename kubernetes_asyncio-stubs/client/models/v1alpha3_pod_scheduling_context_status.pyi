import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha3PodSchedulingContextStatus:
    resource_claims: typing.Optional[
        list[kubernetes_asyncio.client.V1alpha3ResourceClaimSchedulingStatus]
    ]

    def __init__(
        self,
        *,
        resource_claims: typing.Optional[
            list[kubernetes_asyncio.client.V1alpha3ResourceClaimSchedulingStatus]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3PodSchedulingContextStatusDict: ...

class V1alpha3PodSchedulingContextStatusDict(typing.TypedDict, total=False):
    resourceClaims: list[
        kubernetes_asyncio.client.V1alpha3ResourceClaimSchedulingStatusDict
    ]
