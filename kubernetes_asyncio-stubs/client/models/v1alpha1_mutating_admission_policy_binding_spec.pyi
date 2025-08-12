import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1MutatingAdmissionPolicyBindingSpec:
    match_resources: typing.Optional[kubernetes_asyncio.client.V1alpha1MatchResources]
    param_ref: typing.Optional[kubernetes_asyncio.client.V1alpha1ParamRef]
    policy_name: typing.Optional[str]

    def __init__(
        self,
        *,
        match_resources: typing.Optional[
            kubernetes_asyncio.client.V1alpha1MatchResources
        ] = ...,
        param_ref: typing.Optional[kubernetes_asyncio.client.V1alpha1ParamRef] = ...,
        policy_name: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1MutatingAdmissionPolicyBindingSpecDict: ...

class V1alpha1MutatingAdmissionPolicyBindingSpecDict(typing.TypedDict, total=False):
    matchResources: kubernetes_asyncio.client.V1alpha1MatchResourcesDict
    paramRef: kubernetes_asyncio.client.V1alpha1ParamRefDict
    policyName: str
