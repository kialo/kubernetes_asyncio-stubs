import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1IPAddress:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1beta1IPAddressSpec

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes_asyncio.client.V1beta1IPAddressSpec] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1IPAddressDict: ...

class V1beta1IPAddressDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1beta1IPAddressSpecDict
