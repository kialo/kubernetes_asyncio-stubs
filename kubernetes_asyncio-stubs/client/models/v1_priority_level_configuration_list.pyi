import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PriorityLevelConfigurationList:
    api_version: str
    items: list[kubernetes_asyncio.client.V1PriorityLevelConfiguration]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1PriorityLevelConfiguration],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PriorityLevelConfigurationListDict: ...

class V1PriorityLevelConfigurationListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes_asyncio.client.V1PriorityLevelConfigurationDict]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMetaDict
