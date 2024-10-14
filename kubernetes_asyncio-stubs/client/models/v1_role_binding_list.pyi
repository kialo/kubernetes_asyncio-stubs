import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1RoleBindingList:
    api_version: str
    items: list[kubernetes_asyncio.client.V1RoleBinding]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1RoleBinding],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1RoleBindingListDict: ...

class V1RoleBindingListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes_asyncio.client.V1RoleBindingDict]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMetaDict
