import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1NetworkPolicyList:
    api_version: str
    items: list[kubernetes_asyncio.client.V1NetworkPolicy]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1NetworkPolicy],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1NetworkPolicyListDict: ...

class V1NetworkPolicyListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes_asyncio.client.V1NetworkPolicyDict]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMetaDict
