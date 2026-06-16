import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1MutatingAdmissionPolicyBindingList:
    api_version: str
    items: list[kubernetes_asyncio.client.V1beta1MutatingAdmissionPolicyBinding]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1beta1MutatingAdmissionPolicyBinding],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1MutatingAdmissionPolicyBindingListDict: ...

class V1beta1MutatingAdmissionPolicyBindingListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes_asyncio.client.V1beta1MutatingAdmissionPolicyBindingDict]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMetaDict
