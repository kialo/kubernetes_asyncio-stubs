import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PodAffinityTerm:
    label_selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    match_label_keys: typing.Optional[list[str]]
    mismatch_label_keys: typing.Optional[list[str]]
    namespace_selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    namespaces: typing.Optional[list[str]]
    topology_key: str

    def __init__(
        self,
        *,
        label_selector: typing.Optional[
            kubernetes_asyncio.client.V1LabelSelector
        ] = ...,
        match_label_keys: typing.Optional[list[str]] = ...,
        mismatch_label_keys: typing.Optional[list[str]] = ...,
        namespace_selector: typing.Optional[
            kubernetes_asyncio.client.V1LabelSelector
        ] = ...,
        namespaces: typing.Optional[list[str]] = ...,
        topology_key: str,
    ) -> None: ...
    def to_dict(self) -> V1PodAffinityTermDict: ...

class V1PodAffinityTermDict(typing.TypedDict, total=False):
    labelSelector: kubernetes_asyncio.client.V1LabelSelectorDict
    matchLabelKeys: list[str]
    mismatchLabelKeys: list[str]
    namespaceSelector: kubernetes_asyncio.client.V1LabelSelectorDict
    namespaces: list[str]
    topologyKey: str
