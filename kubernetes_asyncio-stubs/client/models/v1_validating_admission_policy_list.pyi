import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ValidatingAdmissionPolicyList:
    api_version: typing.Optional[str]
    items: typing.Optional[list[kubernetes_asyncio.client.V1ValidatingAdmissionPolicy]]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: typing.Optional[
            list[kubernetes_asyncio.client.V1ValidatingAdmissionPolicy]
        ] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ValidatingAdmissionPolicyListDict: ...

class V1ValidatingAdmissionPolicyListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: typing.Optional[
        list[kubernetes_asyncio.client.V1ValidatingAdmissionPolicyDict]
    ]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMetaDict]
