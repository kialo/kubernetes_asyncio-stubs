import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1StorageVersionMigrationList:
    api_version: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V1alpha1StorageVersionMigration]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1alpha1StorageVersionMigration],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1StorageVersionMigrationListDict: ...

class V1alpha1StorageVersionMigrationListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: list[kubernetes_asyncio.client.V1alpha1StorageVersionMigrationDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ListMetaDict]
