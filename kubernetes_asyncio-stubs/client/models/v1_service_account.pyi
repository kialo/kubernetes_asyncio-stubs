import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ServiceAccount:
    api_version: str
    automount_service_account_token: typing.Optional[bool]
    image_pull_secrets: typing.Optional[
        list[kubernetes_asyncio.client.V1LocalObjectReference]
    ]
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    secrets: typing.Optional[list[kubernetes_asyncio.client.V1ObjectReference]]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        automount_service_account_token: typing.Optional[bool] = ...,
        image_pull_secrets: typing.Optional[
            list[kubernetes_asyncio.client.V1LocalObjectReference]
        ] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        secrets: typing.Optional[
            list[kubernetes_asyncio.client.V1ObjectReference]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ServiceAccountDict: ...

class V1ServiceAccountDict(typing.TypedDict, total=False):
    apiVersion: str
    automountServiceAccountToken: bool
    imagePullSecrets: list[kubernetes_asyncio.client.V1LocalObjectReferenceDict]
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    secrets: list[kubernetes_asyncio.client.V1ObjectReferenceDict]
