import kubernetes_asyncio.client
import typing

class StorageV1beta1Api:
    def __init__(
        self,
        api_client: typing.Optional[
            kubernetes_asyncio.client.api_client.ApiClient
        ] = ...,
    ) -> None: ...
    async def get_api_resources(
        self,
    ) -> kubernetes_asyncio.client.V1APIResourceList: ...
    async def list_volume_attributes_class(
        self,
        *,
        pretty: typing.Optional[str] = ...,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1beta1VolumeAttributesClassList: ...
    async def create_volume_attributes_class(
        self,
        body: kubernetes_asyncio.client.V1beta1VolumeAttributesClass,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1beta1VolumeAttributesClass: ...
    async def delete_collection_volume_attributes_class(
        self,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        _continue: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
    ) -> kubernetes_asyncio.client.V1Status: ...
    async def read_volume_attributes_class(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1beta1VolumeAttributesClass: ...
    async def replace_volume_attributes_class(
        self,
        name: str,
        body: kubernetes_asyncio.client.V1beta1VolumeAttributesClass,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1beta1VolumeAttributesClass: ...
    async def delete_volume_attributes_class(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1beta1VolumeAttributesClass: ...
    async def patch_volume_attributes_class(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1beta1VolumeAttributesClass: ...
