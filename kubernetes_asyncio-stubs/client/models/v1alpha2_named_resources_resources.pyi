import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha2NamedResourcesResources:
    instances: list[kubernetes_asyncio.client.V1alpha2NamedResourcesInstance]

    def __init__(
        self,
        *,
        instances: list[kubernetes_asyncio.client.V1alpha2NamedResourcesInstance],
    ) -> None: ...
    def to_dict(self) -> V1alpha2NamedResourcesResourcesDict: ...

class V1alpha2NamedResourcesResourcesDict(typing.TypedDict, total=False):
    instances: list[kubernetes_asyncio.client.V1alpha2NamedResourcesInstanceDict]
