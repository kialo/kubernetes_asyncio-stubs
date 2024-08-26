import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PersistentVolumeClaimStatus:
    access_modes: typing.Optional[list[str]]
    allocated_resource_statuses: typing.Optional[dict[str, str]]
    allocated_resources: typing.Optional[dict[str, str]]
    capacity: typing.Optional[dict[str, str]]
    conditions: typing.Optional[
        list[kubernetes_asyncio.client.V1PersistentVolumeClaimCondition]
    ]
    current_volume_attributes_class_name: typing.Optional[str]
    modify_volume_status: typing.Optional[
        kubernetes_asyncio.client.V1ModifyVolumeStatus
    ]
    phase: typing.Optional[str]

    def __init__(
        self,
        *,
        access_modes: typing.Optional[list[str]] = ...,
        allocated_resource_statuses: typing.Optional[dict[str, str]] = ...,
        allocated_resources: typing.Optional[dict[str, str]] = ...,
        capacity: typing.Optional[dict[str, str]] = ...,
        conditions: typing.Optional[
            list[kubernetes_asyncio.client.V1PersistentVolumeClaimCondition]
        ] = ...,
        current_volume_attributes_class_name: typing.Optional[str] = ...,
        modify_volume_status: typing.Optional[
            kubernetes_asyncio.client.V1ModifyVolumeStatus
        ] = ...,
        phase: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PersistentVolumeClaimStatusDict: ...

class V1PersistentVolumeClaimStatusDict(typing.TypedDict, total=False):
    accessModes: typing.Optional[list[str]]
    allocatedResourceStatuses: typing.Optional[dict[str, str]]
    allocatedResources: typing.Optional[dict[str, str]]
    capacity: typing.Optional[dict[str, str]]
    conditions: typing.Optional[
        list[kubernetes_asyncio.client.V1PersistentVolumeClaimConditionDict]
    ]
    currentVolumeAttributesClassName: typing.Optional[str]
    modifyVolumeStatus: typing.Optional[
        kubernetes_asyncio.client.V1ModifyVolumeStatusDict
    ]
    phase: typing.Optional[str]
