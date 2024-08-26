import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1ValidatingAdmissionPolicy:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[
        kubernetes_asyncio.client.V1beta1ValidatingAdmissionPolicySpec
    ]
    status: typing.Optional[
        kubernetes_asyncio.client.V1beta1ValidatingAdmissionPolicyStatus
    ]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: typing.Optional[
            kubernetes_asyncio.client.V1beta1ValidatingAdmissionPolicySpec
        ] = ...,
        status: typing.Optional[
            kubernetes_asyncio.client.V1beta1ValidatingAdmissionPolicyStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1ValidatingAdmissionPolicyDict: ...

class V1beta1ValidatingAdmissionPolicyDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[
        kubernetes_asyncio.client.V1beta1ValidatingAdmissionPolicySpecDict
    ]
    status: typing.Optional[
        kubernetes_asyncio.client.V1beta1ValidatingAdmissionPolicyStatusDict
    ]
