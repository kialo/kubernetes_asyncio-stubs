import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1IPAddressList:
    api_version: str
    items: list[kubernetes_asyncio.client.V1alpha1IPAddress]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1alpha1IPAddress],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1IPAddressListDict: ...

class V1alpha1IPAddressListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes_asyncio.client.V1alpha1IPAddressDict]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMetaDict
