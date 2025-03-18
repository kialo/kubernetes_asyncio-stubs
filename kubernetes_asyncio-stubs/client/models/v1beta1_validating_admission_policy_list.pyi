import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1ValidatingAdmissionPolicyList:
    api_version: str
    items: typing.Optional[
        list[kubernetes_asyncio.client.V1beta1ValidatingAdmissionPolicy]
    ]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.Optional[
            list[kubernetes_asyncio.client.V1beta1ValidatingAdmissionPolicy]
        ] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1ValidatingAdmissionPolicyListDict: ...

class V1beta1ValidatingAdmissionPolicyListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes_asyncio.client.V1beta1ValidatingAdmissionPolicyDict]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMetaDict
