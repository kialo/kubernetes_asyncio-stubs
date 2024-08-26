import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1IPAddressSpec:
    parent_ref: typing.Optional[kubernetes_asyncio.client.V1alpha1ParentReference]

    def __init__(
        self,
        *,
        parent_ref: typing.Optional[
            kubernetes_asyncio.client.V1alpha1ParentReference
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1IPAddressSpecDict: ...

class V1alpha1IPAddressSpecDict(typing.TypedDict, total=False):
    parentRef: typing.Optional[kubernetes_asyncio.client.V1alpha1ParentReferenceDict]
