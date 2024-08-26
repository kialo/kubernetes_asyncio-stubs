import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta3FlowSchemaSpec:
    distinguisher_method: typing.Optional[
        kubernetes_asyncio.client.V1beta3FlowDistinguisherMethod
    ]
    matching_precedence: typing.Optional[int]
    priority_level_configuration: (
        kubernetes_asyncio.client.V1beta3PriorityLevelConfigurationReference
    )
    rules: typing.Optional[
        list[kubernetes_asyncio.client.V1beta3PolicyRulesWithSubjects]
    ]

    def __init__(
        self,
        *,
        distinguisher_method: typing.Optional[
            kubernetes_asyncio.client.V1beta3FlowDistinguisherMethod
        ] = ...,
        matching_precedence: typing.Optional[int] = ...,
        priority_level_configuration: kubernetes_asyncio.client.V1beta3PriorityLevelConfigurationReference,
        rules: typing.Optional[
            list[kubernetes_asyncio.client.V1beta3PolicyRulesWithSubjects]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta3FlowSchemaSpecDict: ...

class V1beta3FlowSchemaSpecDict(typing.TypedDict, total=False):
    distinguisherMethod: typing.Optional[
        kubernetes_asyncio.client.V1beta3FlowDistinguisherMethodDict
    ]
    matchingPrecedence: typing.Optional[int]
    priorityLevelConfiguration: (
        kubernetes_asyncio.client.V1beta3PriorityLevelConfigurationReferenceDict
    )
    rules: typing.Optional[
        list[kubernetes_asyncio.client.V1beta3PolicyRulesWithSubjectsDict]
    ]
