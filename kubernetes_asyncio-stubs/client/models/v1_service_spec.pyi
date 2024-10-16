import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ServiceSpec:
    allocate_load_balancer_node_ports: typing.Optional[bool]
    cluster_ip: typing.Optional[str]
    cluster_i_ps: typing.Optional[list[str]]
    external_i_ps: typing.Optional[list[str]]
    external_name: typing.Optional[str]
    external_traffic_policy: typing.Optional[str]
    health_check_node_port: typing.Optional[int]
    internal_traffic_policy: typing.Optional[str]
    ip_families: typing.Optional[list[str]]
    ip_family_policy: typing.Optional[str]
    load_balancer_class: typing.Optional[str]
    load_balancer_ip: typing.Optional[str]
    load_balancer_source_ranges: typing.Optional[list[str]]
    ports: typing.Optional[list[kubernetes_asyncio.client.V1ServicePort]]
    publish_not_ready_addresses: typing.Optional[bool]
    selector: typing.Optional[dict[str, str]]
    session_affinity: typing.Optional[str]
    session_affinity_config: typing.Optional[
        kubernetes_asyncio.client.V1SessionAffinityConfig
    ]
    traffic_distribution: typing.Optional[str]
    type: typing.Optional[str]

    def __init__(
        self,
        *,
        allocate_load_balancer_node_ports: typing.Optional[bool] = ...,
        cluster_ip: typing.Optional[str] = ...,
        cluster_i_ps: typing.Optional[list[str]] = ...,
        external_i_ps: typing.Optional[list[str]] = ...,
        external_name: typing.Optional[str] = ...,
        external_traffic_policy: typing.Optional[str] = ...,
        health_check_node_port: typing.Optional[int] = ...,
        internal_traffic_policy: typing.Optional[str] = ...,
        ip_families: typing.Optional[list[str]] = ...,
        ip_family_policy: typing.Optional[str] = ...,
        load_balancer_class: typing.Optional[str] = ...,
        load_balancer_ip: typing.Optional[str] = ...,
        load_balancer_source_ranges: typing.Optional[list[str]] = ...,
        ports: typing.Optional[list[kubernetes_asyncio.client.V1ServicePort]] = ...,
        publish_not_ready_addresses: typing.Optional[bool] = ...,
        selector: typing.Optional[dict[str, str]] = ...,
        session_affinity: typing.Optional[str] = ...,
        session_affinity_config: typing.Optional[
            kubernetes_asyncio.client.V1SessionAffinityConfig
        ] = ...,
        traffic_distribution: typing.Optional[str] = ...,
        type: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ServiceSpecDict: ...

class V1ServiceSpecDict(typing.TypedDict, total=False):
    allocateLoadBalancerNodePorts: bool
    clusterIP: str
    clusterIPs: list[str]
    externalIPs: list[str]
    externalName: str
    externalTrafficPolicy: str
    healthCheckNodePort: int
    internalTrafficPolicy: str
    ipFamilies: list[str]
    ipFamilyPolicy: str
    loadBalancerClass: str
    loadBalancerIP: str
    loadBalancerSourceRanges: list[str]
    ports: list[kubernetes_asyncio.client.V1ServicePortDict]
    publishNotReadyAddresses: bool
    selector: dict[str, str]
    sessionAffinity: str
    sessionAffinityConfig: kubernetes_asyncio.client.V1SessionAffinityConfigDict
    trafficDistribution: str
    type: str
