import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1StorageVersionMigrationStatus:
    conditions: typing.Optional[
        list[kubernetes_asyncio.client.V1alpha1MigrationCondition]
    ]
    resource_version: typing.Optional[str]

    def __init__(
        self,
        *,
        conditions: typing.Optional[
            list[kubernetes_asyncio.client.V1alpha1MigrationCondition]
        ] = ...,
        resource_version: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1StorageVersionMigrationStatusDict: ...

class V1alpha1StorageVersionMigrationStatusDict(typing.TypedDict, total=False):
    conditions: list[kubernetes_asyncio.client.V1alpha1MigrationConditionDict]
    resourceVersion: str
