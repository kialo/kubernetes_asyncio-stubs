import kubernetes_asyncio.client
import typing

class CustomObjectsApi:
    def __init__(
        self,
        api_client: typing.Optional[
            kubernetes_asyncio.client.api_client.ApiClient
        ] = ...,
    ) -> None: ...
    async def get_api_resources(
        self, group: str, version: str
    ) -> kubernetes_asyncio.client.V1APIResourceList: ...
    async def list_cluster_custom_object(
        self,
        group: str,
        version: str,
        plural: str,
        *,
        pretty: typing.Optional[str] = ...,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...,
    ) -> typing.Any: ...
    async def create_cluster_custom_object(
        self,
        group: str,
        version: str,
        plural: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> None: ...
    async def delete_collection_cluster_custom_object(
        self,
        group: str,
        version: str,
        plural: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        label_selector: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
    ) -> typing.Any: ...
    async def list_namespaced_custom_object(
        self,
        group: str,
        version: str,
        namespace: str,
        plural: str,
        *,
        pretty: typing.Optional[str] = ...,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...,
    ) -> typing.Any: ...
    async def create_namespaced_custom_object(
        self,
        group: str,
        version: str,
        namespace: str,
        plural: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> None: ...
    async def delete_collection_namespaced_custom_object(
        self,
        group: str,
        version: str,
        namespace: str,
        plural: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        label_selector: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
    ) -> typing.Any: ...
    async def get_cluster_custom_object(
        self, group: str, version: str, plural: str, name: str
    ) -> typing.Any: ...
    async def replace_cluster_custom_object(
        self,
        group: str,
        version: str,
        plural: str,
        name: str,
        body: typing.Any,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> typing.Any: ...
    async def delete_cluster_custom_object(
        self,
        group: str,
        version: str,
        plural: str,
        name: str,
        *,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
    ) -> typing.Any: ...
    async def patch_cluster_custom_object(
        self,
        group: str,
        version: str,
        plural: str,
        name: str,
        body: typing.Any,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> typing.Any: ...
    async def get_cluster_custom_object_status(
        self, group: str, version: str, plural: str, name: str
    ) -> typing.Any: ...
    async def replace_cluster_custom_object_status(
        self,
        group: str,
        version: str,
        plural: str,
        name: str,
        body: typing.Any,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> typing.Any: ...
    async def patch_cluster_custom_object_status(
        self,
        group: str,
        version: str,
        plural: str,
        name: str,
        body: typing.Any,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> typing.Any: ...
    async def get_cluster_custom_object_scale(
        self, group: str, version: str, plural: str, name: str
    ) -> typing.Any: ...
    async def replace_cluster_custom_object_scale(
        self,
        group: str,
        version: str,
        plural: str,
        name: str,
        body: typing.Any,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> typing.Any: ...
    async def patch_cluster_custom_object_scale(
        self,
        group: str,
        version: str,
        plural: str,
        name: str,
        body: typing.Any,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> typing.Any: ...
    async def get_namespaced_custom_object(
        self, group: str, version: str, namespace: str, plural: str, name: str
    ) -> typing.Any: ...
    async def replace_namespaced_custom_object(
        self,
        group: str,
        version: str,
        namespace: str,
        plural: str,
        name: str,
        body: typing.Any,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> typing.Any: ...
    async def delete_namespaced_custom_object(
        self,
        group: str,
        version: str,
        namespace: str,
        plural: str,
        name: str,
        *,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
    ) -> typing.Any: ...
    async def patch_namespaced_custom_object(
        self,
        group: str,
        version: str,
        namespace: str,
        plural: str,
        name: str,
        body: typing.Any,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> typing.Any: ...
    async def get_namespaced_custom_object_status(
        self, group: str, version: str, namespace: str, plural: str, name: str
    ) -> typing.Any: ...
    async def replace_namespaced_custom_object_status(
        self,
        group: str,
        version: str,
        namespace: str,
        plural: str,
        name: str,
        body: typing.Any,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> typing.Any: ...
    async def patch_namespaced_custom_object_status(
        self,
        group: str,
        version: str,
        namespace: str,
        plural: str,
        name: str,
        body: typing.Any,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> typing.Any: ...
    async def get_namespaced_custom_object_scale(
        self, group: str, version: str, namespace: str, plural: str, name: str
    ) -> typing.Any: ...
    async def replace_namespaced_custom_object_scale(
        self,
        group: str,
        version: str,
        namespace: str,
        plural: str,
        name: str,
        body: typing.Any,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> typing.Any: ...
    async def patch_namespaced_custom_object_scale(
        self,
        group: str,
        version: str,
        namespace: str,
        plural: str,
        name: str,
        body: typing.Any,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> typing.Any: ...
