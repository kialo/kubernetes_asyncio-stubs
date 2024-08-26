import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PolicyRulesWithSubjects:
    non_resource_rules: typing.Optional[
        list[kubernetes_asyncio.client.V1NonResourcePolicyRule]
    ]
    resource_rules: typing.Optional[
        list[kubernetes_asyncio.client.V1ResourcePolicyRule]
    ]
    subjects: list[kubernetes_asyncio.client.FlowcontrolV1Subject]

    def __init__(
        self,
        *,
        non_resource_rules: typing.Optional[
            list[kubernetes_asyncio.client.V1NonResourcePolicyRule]
        ] = ...,
        resource_rules: typing.Optional[
            list[kubernetes_asyncio.client.V1ResourcePolicyRule]
        ] = ...,
        subjects: list[kubernetes_asyncio.client.FlowcontrolV1Subject],
    ) -> None: ...
    def to_dict(self) -> V1PolicyRulesWithSubjectsDict: ...

class V1PolicyRulesWithSubjectsDict(typing.TypedDict, total=False):
    nonResourceRules: typing.Optional[
        list[kubernetes_asyncio.client.V1NonResourcePolicyRuleDict]
    ]
    resourceRules: typing.Optional[
        list[kubernetes_asyncio.client.V1ResourcePolicyRuleDict]
    ]
    subjects: list[kubernetes_asyncio.client.FlowcontrolV1SubjectDict]
