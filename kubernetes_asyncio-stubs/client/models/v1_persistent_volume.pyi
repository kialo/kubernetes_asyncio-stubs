import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PersistentVolume:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1PersistentVolumeSpec
    status: kubernetes_asyncio.client.V1PersistentVolumeStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes_asyncio.client.V1PersistentVolumeSpec] = ...,
        status: typing.Optional[
            kubernetes_asyncio.client.V1PersistentVolumeStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PersistentVolumeDict: ...

class V1PersistentVolumeDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1PersistentVolumeSpecDict
    status: kubernetes_asyncio.client.V1PersistentVolumeStatusDict
