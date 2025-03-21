import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1MatchResources:
    exclude_resource_rules: typing.Optional[
        list[kubernetes_asyncio.client.V1beta1NamedRuleWithOperations]
    ]
    match_policy: typing.Optional[str]
    namespace_selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    object_selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    resource_rules: typing.Optional[
        list[kubernetes_asyncio.client.V1beta1NamedRuleWithOperations]
    ]

    def __init__(
        self,
        *,
        exclude_resource_rules: typing.Optional[
            list[kubernetes_asyncio.client.V1beta1NamedRuleWithOperations]
        ] = ...,
        match_policy: typing.Optional[str] = ...,
        namespace_selector: typing.Optional[
            kubernetes_asyncio.client.V1LabelSelector
        ] = ...,
        object_selector: typing.Optional[
            kubernetes_asyncio.client.V1LabelSelector
        ] = ...,
        resource_rules: typing.Optional[
            list[kubernetes_asyncio.client.V1beta1NamedRuleWithOperations]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1MatchResourcesDict: ...

class V1beta1MatchResourcesDict(typing.TypedDict, total=False):
    excludeResourceRules: list[
        kubernetes_asyncio.client.V1beta1NamedRuleWithOperationsDict
    ]
    matchPolicy: str
    namespaceSelector: kubernetes_asyncio.client.V1LabelSelectorDict
    objectSelector: kubernetes_asyncio.client.V1LabelSelectorDict
    resourceRules: list[kubernetes_asyncio.client.V1beta1NamedRuleWithOperationsDict]
