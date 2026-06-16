import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1MutatingAdmissionPolicySpec:
    failure_policy: typing.Optional[str]
    match_conditions: typing.Optional[
        list[kubernetes_asyncio.client.V1beta1MatchCondition]
    ]
    match_constraints: typing.Optional[kubernetes_asyncio.client.V1beta1MatchResources]
    mutations: typing.Optional[list[kubernetes_asyncio.client.V1beta1Mutation]]
    param_kind: typing.Optional[kubernetes_asyncio.client.V1beta1ParamKind]
    reinvocation_policy: typing.Optional[str]
    variables: typing.Optional[list[kubernetes_asyncio.client.V1beta1Variable]]

    def __init__(
        self,
        *,
        failure_policy: typing.Optional[str] = ...,
        match_conditions: typing.Optional[
            list[kubernetes_asyncio.client.V1beta1MatchCondition]
        ] = ...,
        match_constraints: typing.Optional[
            kubernetes_asyncio.client.V1beta1MatchResources
        ] = ...,
        mutations: typing.Optional[
            list[kubernetes_asyncio.client.V1beta1Mutation]
        ] = ...,
        param_kind: typing.Optional[kubernetes_asyncio.client.V1beta1ParamKind] = ...,
        reinvocation_policy: typing.Optional[str] = ...,
        variables: typing.Optional[
            list[kubernetes_asyncio.client.V1beta1Variable]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1MutatingAdmissionPolicySpecDict: ...

class V1beta1MutatingAdmissionPolicySpecDict(typing.TypedDict, total=False):
    failurePolicy: str
    matchConditions: list[kubernetes_asyncio.client.V1beta1MatchConditionDict]
    matchConstraints: kubernetes_asyncio.client.V1beta1MatchResourcesDict
    mutations: list[kubernetes_asyncio.client.V1beta1MutationDict]
    paramKind: kubernetes_asyncio.client.V1beta1ParamKindDict
    reinvocationPolicy: str
    variables: list[kubernetes_asyncio.client.V1beta1VariableDict]
