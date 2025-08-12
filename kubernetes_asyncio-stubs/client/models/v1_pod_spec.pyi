import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PodSpec:
    active_deadline_seconds: typing.Optional[int]
    affinity: typing.Optional[kubernetes_asyncio.client.V1Affinity]
    automount_service_account_token: typing.Optional[bool]
    containers: list[kubernetes_asyncio.client.V1Container]
    dns_config: typing.Optional[kubernetes_asyncio.client.V1PodDNSConfig]
    dns_policy: typing.Optional[str]
    enable_service_links: typing.Optional[bool]
    ephemeral_containers: typing.Optional[
        list[kubernetes_asyncio.client.V1EphemeralContainer]
    ]
    host_aliases: typing.Optional[list[kubernetes_asyncio.client.V1HostAlias]]
    host_ipc: typing.Optional[bool]
    host_network: typing.Optional[bool]
    host_pid: typing.Optional[bool]
    host_users: typing.Optional[bool]
    hostname: typing.Optional[str]
    image_pull_secrets: typing.Optional[
        list[kubernetes_asyncio.client.V1LocalObjectReference]
    ]
    init_containers: typing.Optional[list[kubernetes_asyncio.client.V1Container]]
    node_name: typing.Optional[str]
    node_selector: typing.Optional[dict[str, str]]
    os: typing.Optional[kubernetes_asyncio.client.V1PodOS]
    overhead: typing.Optional[dict[str, str]]
    preemption_policy: typing.Optional[str]
    priority: typing.Optional[int]
    priority_class_name: typing.Optional[str]
    readiness_gates: typing.Optional[list[kubernetes_asyncio.client.V1PodReadinessGate]]
    resource_claims: typing.Optional[list[kubernetes_asyncio.client.V1PodResourceClaim]]
    resources: typing.Optional[kubernetes_asyncio.client.V1ResourceRequirements]
    restart_policy: typing.Optional[str]
    runtime_class_name: typing.Optional[str]
    scheduler_name: typing.Optional[str]
    scheduling_gates: typing.Optional[
        list[kubernetes_asyncio.client.V1PodSchedulingGate]
    ]
    security_context: typing.Optional[kubernetes_asyncio.client.V1PodSecurityContext]
    service_account: typing.Optional[str]
    service_account_name: typing.Optional[str]
    set_hostname_as_fqdn: typing.Optional[bool]
    share_process_namespace: typing.Optional[bool]
    subdomain: typing.Optional[str]
    termination_grace_period_seconds: typing.Optional[int]
    tolerations: typing.Optional[list[kubernetes_asyncio.client.V1Toleration]]
    topology_spread_constraints: typing.Optional[
        list[kubernetes_asyncio.client.V1TopologySpreadConstraint]
    ]
    volumes: typing.Optional[list[kubernetes_asyncio.client.V1Volume]]

    def __init__(
        self,
        *,
        active_deadline_seconds: typing.Optional[int] = ...,
        affinity: typing.Optional[kubernetes_asyncio.client.V1Affinity] = ...,
        automount_service_account_token: typing.Optional[bool] = ...,
        containers: list[kubernetes_asyncio.client.V1Container],
        dns_config: typing.Optional[kubernetes_asyncio.client.V1PodDNSConfig] = ...,
        dns_policy: typing.Optional[str] = ...,
        enable_service_links: typing.Optional[bool] = ...,
        ephemeral_containers: typing.Optional[
            list[kubernetes_asyncio.client.V1EphemeralContainer]
        ] = ...,
        host_aliases: typing.Optional[
            list[kubernetes_asyncio.client.V1HostAlias]
        ] = ...,
        host_ipc: typing.Optional[bool] = ...,
        host_network: typing.Optional[bool] = ...,
        host_pid: typing.Optional[bool] = ...,
        host_users: typing.Optional[bool] = ...,
        hostname: typing.Optional[str] = ...,
        image_pull_secrets: typing.Optional[
            list[kubernetes_asyncio.client.V1LocalObjectReference]
        ] = ...,
        init_containers: typing.Optional[
            list[kubernetes_asyncio.client.V1Container]
        ] = ...,
        node_name: typing.Optional[str] = ...,
        node_selector: typing.Optional[dict[str, str]] = ...,
        os: typing.Optional[kubernetes_asyncio.client.V1PodOS] = ...,
        overhead: typing.Optional[dict[str, str]] = ...,
        preemption_policy: typing.Optional[str] = ...,
        priority: typing.Optional[int] = ...,
        priority_class_name: typing.Optional[str] = ...,
        readiness_gates: typing.Optional[
            list[kubernetes_asyncio.client.V1PodReadinessGate]
        ] = ...,
        resource_claims: typing.Optional[
            list[kubernetes_asyncio.client.V1PodResourceClaim]
        ] = ...,
        resources: typing.Optional[
            kubernetes_asyncio.client.V1ResourceRequirements
        ] = ...,
        restart_policy: typing.Optional[str] = ...,
        runtime_class_name: typing.Optional[str] = ...,
        scheduler_name: typing.Optional[str] = ...,
        scheduling_gates: typing.Optional[
            list[kubernetes_asyncio.client.V1PodSchedulingGate]
        ] = ...,
        security_context: typing.Optional[
            kubernetes_asyncio.client.V1PodSecurityContext
        ] = ...,
        service_account: typing.Optional[str] = ...,
        service_account_name: typing.Optional[str] = ...,
        set_hostname_as_fqdn: typing.Optional[bool] = ...,
        share_process_namespace: typing.Optional[bool] = ...,
        subdomain: typing.Optional[str] = ...,
        termination_grace_period_seconds: typing.Optional[int] = ...,
        tolerations: typing.Optional[
            list[kubernetes_asyncio.client.V1Toleration]
        ] = ...,
        topology_spread_constraints: typing.Optional[
            list[kubernetes_asyncio.client.V1TopologySpreadConstraint]
        ] = ...,
        volumes: typing.Optional[list[kubernetes_asyncio.client.V1Volume]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PodSpecDict: ...

class V1PodSpecDict(typing.TypedDict, total=False):
    activeDeadlineSeconds: int
    affinity: kubernetes_asyncio.client.V1AffinityDict
    automountServiceAccountToken: bool
    containers: list[kubernetes_asyncio.client.V1ContainerDict]
    dnsConfig: kubernetes_asyncio.client.V1PodDNSConfigDict
    dnsPolicy: str
    enableServiceLinks: bool
    ephemeralContainers: list[kubernetes_asyncio.client.V1EphemeralContainerDict]
    hostAliases: list[kubernetes_asyncio.client.V1HostAliasDict]
    hostIPC: bool
    hostNetwork: bool
    hostPID: bool
    hostUsers: bool
    hostname: str
    imagePullSecrets: list[kubernetes_asyncio.client.V1LocalObjectReferenceDict]
    initContainers: list[kubernetes_asyncio.client.V1ContainerDict]
    nodeName: str
    nodeSelector: dict[str, str]
    os: kubernetes_asyncio.client.V1PodOSDict
    overhead: dict[str, str]
    preemptionPolicy: str
    priority: int
    priorityClassName: str
    readinessGates: list[kubernetes_asyncio.client.V1PodReadinessGateDict]
    resourceClaims: list[kubernetes_asyncio.client.V1PodResourceClaimDict]
    resources: kubernetes_asyncio.client.V1ResourceRequirementsDict
    restartPolicy: str
    runtimeClassName: str
    schedulerName: str
    schedulingGates: list[kubernetes_asyncio.client.V1PodSchedulingGateDict]
    securityContext: kubernetes_asyncio.client.V1PodSecurityContextDict
    serviceAccount: str
    serviceAccountName: str
    setHostnameAsFQDN: bool
    shareProcessNamespace: bool
    subdomain: str
    terminationGracePeriodSeconds: int
    tolerations: list[kubernetes_asyncio.client.V1TolerationDict]
    topologySpreadConstraints: list[
        kubernetes_asyncio.client.V1TopologySpreadConstraintDict
    ]
    volumes: list[kubernetes_asyncio.client.V1VolumeDict]
