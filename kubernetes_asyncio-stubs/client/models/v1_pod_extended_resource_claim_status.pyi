import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PodExtendedResourceClaimStatus:
    request_mappings: list[kubernetes_asyncio.client.V1ContainerExtendedResourceRequest]
    resource_claim_name: str

    def __init__(
        self,
        *,
        request_mappings: list[
            kubernetes_asyncio.client.V1ContainerExtendedResourceRequest
        ],
        resource_claim_name: str,
    ) -> None: ...
    def to_dict(self) -> V1PodExtendedResourceClaimStatusDict: ...

class V1PodExtendedResourceClaimStatusDict(typing.TypedDict, total=False):
    requestMappings: list[
        kubernetes_asyncio.client.V1ContainerExtendedResourceRequestDict
    ]
    resourceClaimName: str
