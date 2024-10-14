import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ResourceQuotaList:
    api_version: str
    items: list[kubernetes_asyncio.client.V1ResourceQuota]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1ResourceQuota],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ResourceQuotaListDict: ...

class V1ResourceQuotaListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes_asyncio.client.V1ResourceQuotaDict]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMetaDict
