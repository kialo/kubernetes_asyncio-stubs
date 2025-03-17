import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ClusterRoleBindingList:
    api_version: str
    items: list[kubernetes_asyncio.client.V1ClusterRoleBinding]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1ClusterRoleBinding],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ClusterRoleBindingListDict: ...

class V1ClusterRoleBindingListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes_asyncio.client.V1ClusterRoleBindingDict]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMetaDict
