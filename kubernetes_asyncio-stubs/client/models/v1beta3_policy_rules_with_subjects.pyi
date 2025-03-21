import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta3PolicyRulesWithSubjects:
    non_resource_rules: typing.Optional[
        list[kubernetes_asyncio.client.V1beta3NonResourcePolicyRule]
    ]
    resource_rules: typing.Optional[
        list[kubernetes_asyncio.client.V1beta3ResourcePolicyRule]
    ]
    subjects: list[kubernetes_asyncio.client.V1beta3Subject]

    def __init__(
        self,
        *,
        non_resource_rules: typing.Optional[
            list[kubernetes_asyncio.client.V1beta3NonResourcePolicyRule]
        ] = ...,
        resource_rules: typing.Optional[
            list[kubernetes_asyncio.client.V1beta3ResourcePolicyRule]
        ] = ...,
        subjects: list[kubernetes_asyncio.client.V1beta3Subject],
    ) -> None: ...
    def to_dict(self) -> V1beta3PolicyRulesWithSubjectsDict: ...

class V1beta3PolicyRulesWithSubjectsDict(typing.TypedDict, total=False):
    nonResourceRules: list[kubernetes_asyncio.client.V1beta3NonResourcePolicyRuleDict]
    resourceRules: list[kubernetes_asyncio.client.V1beta3ResourcePolicyRuleDict]
    subjects: list[kubernetes_asyncio.client.V1beta3SubjectDict]
