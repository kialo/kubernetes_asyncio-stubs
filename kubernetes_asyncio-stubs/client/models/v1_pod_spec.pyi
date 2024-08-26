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
    activeDeadlineSeconds: typing.Optional[int]
    affinity: typing.Optional[kubernetes_asyncio.client.V1AffinityDict]
    automountServiceAccountToken: typing.Optional[bool]
    containers: list[kubernetes_asyncio.client.V1ContainerDict]
    dnsConfig: typing.Optional[kubernetes_asyncio.client.V1PodDNSConfigDict]
    dnsPolicy: typing.Optional[str]
    enableServiceLinks: typing.Optional[bool]
    ephemeralContainers: typing.Optional[
        list[kubernetes_asyncio.client.V1EphemeralContainerDict]
    ]
    hostAliases: typing.Optional[list[kubernetes_asyncio.client.V1HostAliasDict]]
    hostIPC: typing.Optional[bool]
    hostNetwork: typing.Optional[bool]
    hostPID: typing.Optional[bool]
    hostUsers: typing.Optional[bool]
    hostname: typing.Optional[str]
    imagePullSecrets: typing.Optional[
        list[kubernetes_asyncio.client.V1LocalObjectReferenceDict]
    ]
    initContainers: typing.Optional[list[kubernetes_asyncio.client.V1ContainerDict]]
    nodeName: typing.Optional[str]
    nodeSelector: typing.Optional[dict[str, str]]
    os: typing.Optional[kubernetes_asyncio.client.V1PodOSDict]
    overhead: typing.Optional[dict[str, str]]
    preemptionPolicy: typing.Optional[str]
    priority: typing.Optional[int]
    priorityClassName: typing.Optional[str]
    readinessGates: typing.Optional[
        list[kubernetes_asyncio.client.V1PodReadinessGateDict]
    ]
    resourceClaims: typing.Optional[
        list[kubernetes_asyncio.client.V1PodResourceClaimDict]
    ]
    restartPolicy: typing.Optional[str]
    runtimeClassName: typing.Optional[str]
    schedulerName: typing.Optional[str]
    schedulingGates: typing.Optional[
        list[kubernetes_asyncio.client.V1PodSchedulingGateDict]
    ]
    securityContext: typing.Optional[kubernetes_asyncio.client.V1PodSecurityContextDict]
    serviceAccount: typing.Optional[str]
    serviceAccountName: typing.Optional[str]
    setHostnameAsFQDN: typing.Optional[bool]
    shareProcessNamespace: typing.Optional[bool]
    subdomain: typing.Optional[str]
    terminationGracePeriodSeconds: typing.Optional[int]
    tolerations: typing.Optional[list[kubernetes_asyncio.client.V1TolerationDict]]
    topologySpreadConstraints: typing.Optional[
        list[kubernetes_asyncio.client.V1TopologySpreadConstraintDict]
    ]
    volumes: typing.Optional[list[kubernetes_asyncio.client.V1VolumeDict]]
