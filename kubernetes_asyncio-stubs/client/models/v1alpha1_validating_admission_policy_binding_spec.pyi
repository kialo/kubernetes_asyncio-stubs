import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1ValidatingAdmissionPolicyBindingSpec:
    match_resources: typing.Optional[kubernetes_asyncio.client.V1alpha1MatchResources]
    param_ref: typing.Optional[kubernetes_asyncio.client.V1alpha1ParamRef]
    policy_name: typing.Optional[str]
    validation_actions: typing.Optional[list[str]]

    def __init__(
        self,
        *,
        match_resources: typing.Optional[
            kubernetes_asyncio.client.V1alpha1MatchResources
        ] = ...,
        param_ref: typing.Optional[kubernetes_asyncio.client.V1alpha1ParamRef] = ...,
        policy_name: typing.Optional[str] = ...,
        validation_actions: typing.Optional[list[str]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1ValidatingAdmissionPolicyBindingSpecDict: ...

class V1alpha1ValidatingAdmissionPolicyBindingSpecDict(typing.TypedDict, total=False):
    matchResources: typing.Optional[
        kubernetes_asyncio.client.V1alpha1MatchResourcesDict
    ]
    paramRef: typing.Optional[kubernetes_asyncio.client.V1alpha1ParamRefDict]
    policyName: typing.Optional[str]
    validationActions: typing.Optional[list[str]]
