import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1ValidatingAdmissionPolicy:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1alpha1ValidatingAdmissionPolicySpec
    status: kubernetes_asyncio.client.V1alpha1ValidatingAdmissionPolicyStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: typing.Optional[
            kubernetes_asyncio.client.V1alpha1ValidatingAdmissionPolicySpec
        ] = ...,
        status: typing.Optional[
            kubernetes_asyncio.client.V1alpha1ValidatingAdmissionPolicyStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1ValidatingAdmissionPolicyDict: ...

class V1alpha1ValidatingAdmissionPolicyDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1alpha1ValidatingAdmissionPolicySpecDict
    status: kubernetes_asyncio.client.V1alpha1ValidatingAdmissionPolicyStatusDict
