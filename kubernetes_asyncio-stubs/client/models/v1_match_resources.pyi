import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1MatchResources:
    exclude_resource_rules: typing.Optional[
        list[kubernetes_asyncio.client.V1NamedRuleWithOperations]
    ]
    match_policy: typing.Optional[str]
    namespace_selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    object_selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    resource_rules: typing.Optional[
        list[kubernetes_asyncio.client.V1NamedRuleWithOperations]
    ]

    def __init__(
        self,
        *,
        exclude_resource_rules: typing.Optional[
            list[kubernetes_asyncio.client.V1NamedRuleWithOperations]
        ] = ...,
        match_policy: typing.Optional[str] = ...,
        namespace_selector: typing.Optional[
            kubernetes_asyncio.client.V1LabelSelector
        ] = ...,
        object_selector: typing.Optional[
            kubernetes_asyncio.client.V1LabelSelector
        ] = ...,
        resource_rules: typing.Optional[
            list[kubernetes_asyncio.client.V1NamedRuleWithOperations]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1MatchResourcesDict: ...

class V1MatchResourcesDict(typing.TypedDict, total=False):
    excludeResourceRules: typing.Optional[
        list[kubernetes_asyncio.client.V1NamedRuleWithOperationsDict]
    ]
    matchPolicy: typing.Optional[str]
    namespaceSelector: typing.Optional[kubernetes_asyncio.client.V1LabelSelectorDict]
    objectSelector: typing.Optional[kubernetes_asyncio.client.V1LabelSelectorDict]
    resourceRules: typing.Optional[
        list[kubernetes_asyncio.client.V1NamedRuleWithOperationsDict]
    ]
