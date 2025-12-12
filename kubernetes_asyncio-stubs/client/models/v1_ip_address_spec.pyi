import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1IPAddressSpec:
    parent_ref: kubernetes_asyncio.client.V1ParentReference

    def __init__(
        self, *, parent_ref: kubernetes_asyncio.client.V1ParentReference
    ) -> None: ...
    def to_dict(self) -> V1IPAddressSpecDict: ...

class V1IPAddressSpecDict(typing.TypedDict, total=False):
    parentRef: kubernetes_asyncio.client.V1ParentReferenceDict
