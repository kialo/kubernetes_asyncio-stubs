import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1TopologySpreadConstraint:
    label_selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    match_label_keys: typing.Optional[list[str]]
    max_skew: int
    min_domains: typing.Optional[int]
    node_affinity_policy: typing.Optional[str]
    node_taints_policy: typing.Optional[str]
    topology_key: str
    when_unsatisfiable: str

    def __init__(
        self,
        *,
        label_selector: typing.Optional[
            kubernetes_asyncio.client.V1LabelSelector
        ] = ...,
        match_label_keys: typing.Optional[list[str]] = ...,
        max_skew: int,
        min_domains: typing.Optional[int] = ...,
        node_affinity_policy: typing.Optional[str] = ...,
        node_taints_policy: typing.Optional[str] = ...,
        topology_key: str,
        when_unsatisfiable: str,
    ) -> None: ...
    def to_dict(self) -> V1TopologySpreadConstraintDict: ...

class V1TopologySpreadConstraintDict(typing.TypedDict, total=False):
    labelSelector: kubernetes_asyncio.client.V1LabelSelectorDict
    matchLabelKeys: list[str]
    maxSkew: int
    minDomains: int
    nodeAffinityPolicy: str
    nodeTaintsPolicy: str
    topologyKey: str
    whenUnsatisfiable: str
