import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CSIPersistentVolumeSource:
    controller_expand_secret_ref: typing.Optional[
        kubernetes_asyncio.client.V1SecretReference
    ]
    controller_publish_secret_ref: typing.Optional[
        kubernetes_asyncio.client.V1SecretReference
    ]
    driver: str
    fs_type: typing.Optional[str]
    node_expand_secret_ref: typing.Optional[kubernetes_asyncio.client.V1SecretReference]
    node_publish_secret_ref: typing.Optional[
        kubernetes_asyncio.client.V1SecretReference
    ]
    node_stage_secret_ref: typing.Optional[kubernetes_asyncio.client.V1SecretReference]
    read_only: typing.Optional[bool]
    volume_attributes: typing.Optional[dict[str, str]]
    volume_handle: str

    def __init__(
        self,
        *,
        controller_expand_secret_ref: typing.Optional[
            kubernetes_asyncio.client.V1SecretReference
        ] = ...,
        controller_publish_secret_ref: typing.Optional[
            kubernetes_asyncio.client.V1SecretReference
        ] = ...,
        driver: str,
        fs_type: typing.Optional[str] = ...,
        node_expand_secret_ref: typing.Optional[
            kubernetes_asyncio.client.V1SecretReference
        ] = ...,
        node_publish_secret_ref: typing.Optional[
            kubernetes_asyncio.client.V1SecretReference
        ] = ...,
        node_stage_secret_ref: typing.Optional[
            kubernetes_asyncio.client.V1SecretReference
        ] = ...,
        read_only: typing.Optional[bool] = ...,
        volume_attributes: typing.Optional[dict[str, str]] = ...,
        volume_handle: str,
    ) -> None: ...
    def to_dict(self) -> V1CSIPersistentVolumeSourceDict: ...

class V1CSIPersistentVolumeSourceDict(typing.TypedDict, total=False):
    controllerExpandSecretRef: kubernetes_asyncio.client.V1SecretReferenceDict
    controllerPublishSecretRef: kubernetes_asyncio.client.V1SecretReferenceDict
    driver: str
    fsType: str
    nodeExpandSecretRef: kubernetes_asyncio.client.V1SecretReferenceDict
    nodePublishSecretRef: kubernetes_asyncio.client.V1SecretReferenceDict
    nodeStageSecretRef: kubernetes_asyncio.client.V1SecretReferenceDict
    readOnly: bool
    volumeAttributes: dict[str, str]
    volumeHandle: str
