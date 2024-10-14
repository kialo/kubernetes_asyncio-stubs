import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1ValidatingAdmissionPolicySpec:
    audit_annotations: typing.Optional[
        list[kubernetes_asyncio.client.V1alpha1AuditAnnotation]
    ]
    failure_policy: typing.Optional[str]
    match_conditions: typing.Optional[
        list[kubernetes_asyncio.client.V1alpha1MatchCondition]
    ]
    match_constraints: typing.Optional[kubernetes_asyncio.client.V1alpha1MatchResources]
    param_kind: typing.Optional[kubernetes_asyncio.client.V1alpha1ParamKind]
    validations: typing.Optional[list[kubernetes_asyncio.client.V1alpha1Validation]]
    variables: typing.Optional[list[kubernetes_asyncio.client.V1alpha1Variable]]

    def __init__(
        self,
        *,
        audit_annotations: typing.Optional[
            list[kubernetes_asyncio.client.V1alpha1AuditAnnotation]
        ] = ...,
        failure_policy: typing.Optional[str] = ...,
        match_conditions: typing.Optional[
            list[kubernetes_asyncio.client.V1alpha1MatchCondition]
        ] = ...,
        match_constraints: typing.Optional[
            kubernetes_asyncio.client.V1alpha1MatchResources
        ] = ...,
        param_kind: typing.Optional[kubernetes_asyncio.client.V1alpha1ParamKind] = ...,
        validations: typing.Optional[
            list[kubernetes_asyncio.client.V1alpha1Validation]
        ] = ...,
        variables: typing.Optional[
            list[kubernetes_asyncio.client.V1alpha1Variable]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1ValidatingAdmissionPolicySpecDict: ...

class V1alpha1ValidatingAdmissionPolicySpecDict(typing.TypedDict, total=False):
    auditAnnotations: list[kubernetes_asyncio.client.V1alpha1AuditAnnotationDict]
    failurePolicy: str
    matchConditions: list[kubernetes_asyncio.client.V1alpha1MatchConditionDict]
    matchConstraints: kubernetes_asyncio.client.V1alpha1MatchResourcesDict
    paramKind: kubernetes_asyncio.client.V1alpha1ParamKindDict
    validations: list[kubernetes_asyncio.client.V1alpha1ValidationDict]
    variables: list[kubernetes_asyncio.client.V1alpha1VariableDict]
