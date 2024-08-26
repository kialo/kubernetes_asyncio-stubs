import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ValidatingAdmissionPolicy:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V1ValidatingAdmissionPolicySpec]
    status: typing.Optional[kubernetes_asyncio.client.V1ValidatingAdmissionPolicyStatus]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: typing.Optional[
            kubernetes_asyncio.client.V1ValidatingAdmissionPolicySpec
        ] = ...,
        status: typing.Optional[
            kubernetes_asyncio.client.V1ValidatingAdmissionPolicyStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ValidatingAdmissionPolicyDict: ...

class V1ValidatingAdmissionPolicyDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V1ValidatingAdmissionPolicySpecDict]
    status: typing.Optional[
        kubernetes_asyncio.client.V1ValidatingAdmissionPolicyStatusDict
    ]
