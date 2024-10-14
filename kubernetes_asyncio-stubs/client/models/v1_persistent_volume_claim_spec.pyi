import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PersistentVolumeClaimSpec:
    access_modes: typing.Optional[list[str]]
    data_source: typing.Optional[kubernetes_asyncio.client.V1TypedLocalObjectReference]
    data_source_ref: typing.Optional[kubernetes_asyncio.client.V1TypedObjectReference]
    resources: typing.Optional[kubernetes_asyncio.client.V1VolumeResourceRequirements]
    selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]
    storage_class_name: typing.Optional[str]
    volume_attributes_class_name: typing.Optional[str]
    volume_mode: typing.Optional[str]
    volume_name: typing.Optional[str]

    def __init__(
        self,
        *,
        access_modes: typing.Optional[list[str]] = ...,
        data_source: typing.Optional[
            kubernetes_asyncio.client.V1TypedLocalObjectReference
        ] = ...,
        data_source_ref: typing.Optional[
            kubernetes_asyncio.client.V1TypedObjectReference
        ] = ...,
        resources: typing.Optional[
            kubernetes_asyncio.client.V1VolumeResourceRequirements
        ] = ...,
        selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector] = ...,
        storage_class_name: typing.Optional[str] = ...,
        volume_attributes_class_name: typing.Optional[str] = ...,
        volume_mode: typing.Optional[str] = ...,
        volume_name: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PersistentVolumeClaimSpecDict: ...

class V1PersistentVolumeClaimSpecDict(typing.TypedDict, total=False):
    accessModes: list[str]
    dataSource: kubernetes_asyncio.client.V1TypedLocalObjectReferenceDict
    dataSourceRef: kubernetes_asyncio.client.V1TypedObjectReferenceDict
    resources: kubernetes_asyncio.client.V1VolumeResourceRequirementsDict
    selector: kubernetes_asyncio.client.V1LabelSelectorDict
    storageClassName: str
    volumeAttributesClassName: str
    volumeMode: str
    volumeName: str
