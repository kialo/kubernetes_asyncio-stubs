import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1MutatingAdmissionPolicy:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1alpha1MutatingAdmissionPolicySpec

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: typing.Optional[
            kubernetes_asyncio.client.V1alpha1MutatingAdmissionPolicySpec
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1MutatingAdmissionPolicyDict: ...

class V1alpha1MutatingAdmissionPolicyDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1alpha1MutatingAdmissionPolicySpecDict
