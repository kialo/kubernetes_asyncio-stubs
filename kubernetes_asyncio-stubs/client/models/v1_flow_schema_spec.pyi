import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1FlowSchemaSpec:
    distinguisher_method: typing.Optional[
        kubernetes_asyncio.client.V1FlowDistinguisherMethod
    ]
    matching_precedence: typing.Optional[int]
    priority_level_configuration: (
        kubernetes_asyncio.client.V1PriorityLevelConfigurationReference
    )
    rules: typing.Optional[list[kubernetes_asyncio.client.V1PolicyRulesWithSubjects]]

    def __init__(
        self,
        *,
        distinguisher_method: typing.Optional[
            kubernetes_asyncio.client.V1FlowDistinguisherMethod
        ] = ...,
        matching_precedence: typing.Optional[int] = ...,
        priority_level_configuration: kubernetes_asyncio.client.V1PriorityLevelConfigurationReference,
        rules: typing.Optional[
            list[kubernetes_asyncio.client.V1PolicyRulesWithSubjects]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1FlowSchemaSpecDict: ...

class V1FlowSchemaSpecDict(typing.TypedDict, total=False):
    distinguisherMethod: typing.Optional[
        kubernetes_asyncio.client.V1FlowDistinguisherMethodDict
    ]
    matchingPrecedence: typing.Optional[int]
    priorityLevelConfiguration: (
        kubernetes_asyncio.client.V1PriorityLevelConfigurationReferenceDict
    )
    rules: typing.Optional[
        list[kubernetes_asyncio.client.V1PolicyRulesWithSubjectsDict]
    ]
