import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1StatefulSetSpec:
    min_ready_seconds: typing.Optional[int]
    ordinals: typing.Optional[kubernetes_asyncio.client.V1StatefulSetOrdinals]
    persistent_volume_claim_retention_policy: typing.Optional[
        kubernetes_asyncio.client.V1StatefulSetPersistentVolumeClaimRetentionPolicy
    ]
    pod_management_policy: typing.Optional[str]
    replicas: typing.Optional[int]
    revision_history_limit: typing.Optional[int]
    selector: kubernetes_asyncio.client.V1LabelSelector
    service_name: typing.Optional[str]
    template: kubernetes_asyncio.client.V1PodTemplateSpec
    update_strategy: typing.Optional[
        kubernetes_asyncio.client.V1StatefulSetUpdateStrategy
    ]
    volume_claim_templates: typing.Optional[
        list[kubernetes_asyncio.client.V1PersistentVolumeClaim]
    ]

    def __init__(
        self,
        *,
        min_ready_seconds: typing.Optional[int] = ...,
        ordinals: typing.Optional[
            kubernetes_asyncio.client.V1StatefulSetOrdinals
        ] = ...,
        persistent_volume_claim_retention_policy: typing.Optional[
            kubernetes_asyncio.client.V1StatefulSetPersistentVolumeClaimRetentionPolicy
        ] = ...,
        pod_management_policy: typing.Optional[str] = ...,
        replicas: typing.Optional[int] = ...,
        revision_history_limit: typing.Optional[int] = ...,
        selector: kubernetes_asyncio.client.V1LabelSelector,
        service_name: typing.Optional[str] = ...,
        template: kubernetes_asyncio.client.V1PodTemplateSpec,
        update_strategy: typing.Optional[
            kubernetes_asyncio.client.V1StatefulSetUpdateStrategy
        ] = ...,
        volume_claim_templates: typing.Optional[
            list[kubernetes_asyncio.client.V1PersistentVolumeClaim]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1StatefulSetSpecDict: ...

class V1StatefulSetSpecDict(typing.TypedDict, total=False):
    minReadySeconds: int
    ordinals: kubernetes_asyncio.client.V1StatefulSetOrdinalsDict
    persistentVolumeClaimRetentionPolicy: (
        kubernetes_asyncio.client.V1StatefulSetPersistentVolumeClaimRetentionPolicyDict
    )
    podManagementPolicy: str
    replicas: int
    revisionHistoryLimit: int
    selector: kubernetes_asyncio.client.V1LabelSelectorDict
    serviceName: str
    template: kubernetes_asyncio.client.V1PodTemplateSpecDict
    updateStrategy: kubernetes_asyncio.client.V1StatefulSetUpdateStrategyDict
    volumeClaimTemplates: list[kubernetes_asyncio.client.V1PersistentVolumeClaimDict]
