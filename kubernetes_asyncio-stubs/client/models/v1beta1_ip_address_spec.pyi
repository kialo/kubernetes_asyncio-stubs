import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1IPAddressSpec:
    parent_ref: kubernetes_asyncio.client.V1beta1ParentReference

    def __init__(
        self, *, parent_ref: kubernetes_asyncio.client.V1beta1ParentReference
    ) -> None: ...
    def to_dict(self) -> V1beta1IPAddressSpecDict: ...

class V1beta1IPAddressSpecDict(typing.TypedDict, total=False):
    parentRef: kubernetes_asyncio.client.V1beta1ParentReferenceDict
