import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1ValidatingAdmissionPolicySpec:
    audit_annotations: typing.Optional[
        list[kubernetes_asyncio.client.V1beta1AuditAnnotation]
    ]
    failure_policy: typing.Optional[str]
    match_conditions: typing.Optional[
        list[kubernetes_asyncio.client.V1beta1MatchCondition]
    ]
    match_constraints: typing.Optional[kubernetes_asyncio.client.V1beta1MatchResources]
    param_kind: typing.Optional[kubernetes_asyncio.client.V1beta1ParamKind]
    validations: typing.Optional[list[kubernetes_asyncio.client.V1beta1Validation]]
    variables: typing.Optional[list[kubernetes_asyncio.client.V1beta1Variable]]

    def __init__(
        self,
        *,
        audit_annotations: typing.Optional[
            list[kubernetes_asyncio.client.V1beta1AuditAnnotation]
        ] = ...,
        failure_policy: typing.Optional[str] = ...,
        match_conditions: typing.Optional[
            list[kubernetes_asyncio.client.V1beta1MatchCondition]
        ] = ...,
        match_constraints: typing.Optional[
            kubernetes_asyncio.client.V1beta1MatchResources
        ] = ...,
        param_kind: typing.Optional[kubernetes_asyncio.client.V1beta1ParamKind] = ...,
        validations: typing.Optional[
            list[kubernetes_asyncio.client.V1beta1Validation]
        ] = ...,
        variables: typing.Optional[
            list[kubernetes_asyncio.client.V1beta1Variable]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1ValidatingAdmissionPolicySpecDict: ...

class V1beta1ValidatingAdmissionPolicySpecDict(typing.TypedDict, total=False):
    auditAnnotations: list[kubernetes_asyncio.client.V1beta1AuditAnnotationDict]
    failurePolicy: str
    matchConditions: list[kubernetes_asyncio.client.V1beta1MatchConditionDict]
    matchConstraints: kubernetes_asyncio.client.V1beta1MatchResourcesDict
    paramKind: kubernetes_asyncio.client.V1beta1ParamKindDict
    validations: list[kubernetes_asyncio.client.V1beta1ValidationDict]
    variables: list[kubernetes_asyncio.client.V1beta1VariableDict]
