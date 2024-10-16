import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CephFSPersistentVolumeSource:
    monitors: list[str]
    path: typing.Optional[str]
    read_only: typing.Optional[bool]
    secret_file: typing.Optional[str]
    secret_ref: typing.Optional[kubernetes_asyncio.client.V1SecretReference]
    user: typing.Optional[str]

    def __init__(
        self,
        *,
        monitors: list[str],
        path: typing.Optional[str] = ...,
        read_only: typing.Optional[bool] = ...,
        secret_file: typing.Optional[str] = ...,
        secret_ref: typing.Optional[kubernetes_asyncio.client.V1SecretReference] = ...,
        user: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1CephFSPersistentVolumeSourceDict: ...

class V1CephFSPersistentVolumeSourceDict(typing.TypedDict, total=False):
    monitors: list[str]
    path: str
    readOnly: bool
    secretFile: str
    secretRef: kubernetes_asyncio.client.V1SecretReferenceDict
    user: str
