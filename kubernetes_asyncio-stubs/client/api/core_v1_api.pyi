import kubernetes_asyncio.client
import typing

class CoreV1Api:
    def __init__(
        self,
        api_client: typing.Optional[
            kubernetes_asyncio.client.api_client.ApiClient
        ] = ...,
    ) -> None: ...
    async def get_api_resources(
        self,
    ) -> kubernetes_asyncio.client.V1APIResourceList: ...
    async def list_component_status(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        pretty: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1ComponentStatusList: ...
    async def read_component_status(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1ComponentStatus: ...
    async def list_config_map_for_all_namespaces(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        pretty: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1ConfigMapList: ...
    async def list_endpoints_for_all_namespaces(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        pretty: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1EndpointsList: ...
    async def list_event_for_all_namespaces(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        pretty: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.CoreV1EventList: ...
    async def list_limit_range_for_all_namespaces(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        pretty: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1LimitRangeList: ...
    async def list_namespace(
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
    ) -> kubernetes_asyncio.client.V1NamespaceList: ...
    async def create_namespace(
        self,
        body: kubernetes_asyncio.client.V1Namespace,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Namespace: ...
    async def create_namespaced_binding(
        self,
        namespace: str,
        body: kubernetes_asyncio.client.V1Binding,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Binding: ...
    async def list_namespaced_config_map(
        self,
        namespace: str,
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
    ) -> kubernetes_asyncio.client.V1ConfigMapList: ...
    async def create_namespaced_config_map(
        self,
        namespace: str,
        body: kubernetes_asyncio.client.V1ConfigMap,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1ConfigMap: ...
    async def delete_collection_namespaced_config_map(
        self,
        namespace: str,
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
    async def read_namespaced_config_map(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1ConfigMap: ...
    async def replace_namespaced_config_map(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1ConfigMap,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1ConfigMap: ...
    async def delete_namespaced_config_map(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Status: ...
    async def patch_namespaced_config_map(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1ConfigMap: ...
    async def list_namespaced_endpoints(
        self,
        namespace: str,
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
    ) -> kubernetes_asyncio.client.V1EndpointsList: ...
    async def create_namespaced_endpoints(
        self,
        namespace: str,
        body: kubernetes_asyncio.client.V1Endpoints,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Endpoints: ...
    async def delete_collection_namespaced_endpoints(
        self,
        namespace: str,
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
    async def read_namespaced_endpoints(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1Endpoints: ...
    async def replace_namespaced_endpoints(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1Endpoints,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Endpoints: ...
    async def delete_namespaced_endpoints(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Status: ...
    async def patch_namespaced_endpoints(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1Endpoints: ...
    async def list_namespaced_event(
        self,
        namespace: str,
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
    ) -> kubernetes_asyncio.client.CoreV1EventList: ...
    async def create_namespaced_event(
        self,
        namespace: str,
        body: kubernetes_asyncio.client.CoreV1Event,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.CoreV1Event: ...
    async def delete_collection_namespaced_event(
        self,
        namespace: str,
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
    async def read_namespaced_event(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.CoreV1Event: ...
    async def replace_namespaced_event(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.CoreV1Event,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.CoreV1Event: ...
    async def delete_namespaced_event(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Status: ...
    async def patch_namespaced_event(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.CoreV1Event: ...
    async def list_namespaced_limit_range(
        self,
        namespace: str,
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
    ) -> kubernetes_asyncio.client.V1LimitRangeList: ...
    async def create_namespaced_limit_range(
        self,
        namespace: str,
        body: kubernetes_asyncio.client.V1LimitRange,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1LimitRange: ...
    async def delete_collection_namespaced_limit_range(
        self,
        namespace: str,
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
    async def read_namespaced_limit_range(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1LimitRange: ...
    async def replace_namespaced_limit_range(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1LimitRange,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1LimitRange: ...
    async def delete_namespaced_limit_range(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Status: ...
    async def patch_namespaced_limit_range(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1LimitRange: ...
    async def list_namespaced_persistent_volume_claim(
        self,
        namespace: str,
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
    ) -> kubernetes_asyncio.client.V1PersistentVolumeClaimList: ...
    async def create_namespaced_persistent_volume_claim(
        self,
        namespace: str,
        body: kubernetes_asyncio.client.V1PersistentVolumeClaim,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1PersistentVolumeClaim: ...
    async def delete_collection_namespaced_persistent_volume_claim(
        self,
        namespace: str,
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
    async def read_namespaced_persistent_volume_claim(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1PersistentVolumeClaim: ...
    async def replace_namespaced_persistent_volume_claim(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1PersistentVolumeClaim,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1PersistentVolumeClaim: ...
    async def delete_namespaced_persistent_volume_claim(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1PersistentVolumeClaim: ...
    async def patch_namespaced_persistent_volume_claim(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1PersistentVolumeClaim: ...
    async def read_namespaced_persistent_volume_claim_status(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1PersistentVolumeClaim: ...
    async def replace_namespaced_persistent_volume_claim_status(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1PersistentVolumeClaim,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1PersistentVolumeClaim: ...
    async def patch_namespaced_persistent_volume_claim_status(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1PersistentVolumeClaim: ...
    async def list_namespaced_pod(
        self,
        namespace: str,
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
    ) -> kubernetes_asyncio.client.V1PodList: ...
    async def create_namespaced_pod(
        self,
        namespace: str,
        body: kubernetes_asyncio.client.V1Pod,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Pod: ...
    async def delete_collection_namespaced_pod(
        self,
        namespace: str,
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
    async def read_namespaced_pod(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1Pod: ...
    async def replace_namespaced_pod(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1Pod,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Pod: ...
    async def delete_namespaced_pod(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Pod: ...
    async def patch_namespaced_pod(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1Pod: ...
    async def connect_get_namespaced_pod_attach(
        self,
        name: str,
        namespace: str,
        *,
        container: typing.Optional[str] = ...,
        stderr: typing.Optional[bool] = ...,
        stdin: typing.Optional[bool] = ...,
        stdout: typing.Optional[bool] = ...,
        tty: typing.Optional[bool] = ...,
    ) -> str: ...
    async def connect_post_namespaced_pod_attach(
        self,
        name: str,
        namespace: str,
        *,
        container: typing.Optional[str] = ...,
        stderr: typing.Optional[bool] = ...,
        stdin: typing.Optional[bool] = ...,
        stdout: typing.Optional[bool] = ...,
        tty: typing.Optional[bool] = ...,
    ) -> str: ...
    async def create_namespaced_pod_binding(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1Binding,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Binding: ...
    async def read_namespaced_pod_ephemeralcontainers(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1Pod: ...
    async def replace_namespaced_pod_ephemeralcontainers(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1Pod,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Pod: ...
    async def patch_namespaced_pod_ephemeralcontainers(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1Pod: ...
    async def create_namespaced_pod_eviction(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1Eviction,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Eviction: ...
    async def connect_get_namespaced_pod_exec(
        self,
        name: str,
        namespace: str,
        *,
        command: typing.Optional[str] = ...,
        container: typing.Optional[str] = ...,
        stderr: typing.Optional[bool] = ...,
        stdin: typing.Optional[bool] = ...,
        stdout: typing.Optional[bool] = ...,
        tty: typing.Optional[bool] = ...,
    ) -> str: ...
    async def connect_post_namespaced_pod_exec(
        self,
        name: str,
        namespace: str,
        *,
        command: typing.Optional[str] = ...,
        container: typing.Optional[str] = ...,
        stderr: typing.Optional[bool] = ...,
        stdin: typing.Optional[bool] = ...,
        stdout: typing.Optional[bool] = ...,
        tty: typing.Optional[bool] = ...,
    ) -> str: ...
    async def read_namespaced_pod_log(
        self,
        name: str,
        namespace: str,
        *,
        container: typing.Optional[str] = ...,
        follow: typing.Optional[bool] = ...,
        insecure_skip_tls_verify_backend: typing.Optional[bool] = ...,
        limit_bytes: typing.Optional[int] = ...,
        pretty: typing.Optional[str] = ...,
        previous: typing.Optional[bool] = ...,
        since_seconds: typing.Optional[int] = ...,
        tail_lines: typing.Optional[int] = ...,
        timestamps: typing.Optional[bool] = ...,
    ) -> str: ...
    async def connect_get_namespaced_pod_portforward(
        self, name: str, namespace: str, *, ports: typing.Optional[int] = ...
    ) -> str: ...
    async def connect_post_namespaced_pod_portforward(
        self, name: str, namespace: str, *, ports: typing.Optional[int] = ...
    ) -> str: ...
    async def connect_get_namespaced_pod_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_put_namespaced_pod_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_post_namespaced_pod_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_delete_namespaced_pod_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_options_namespaced_pod_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_head_namespaced_pod_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_patch_namespaced_pod_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_get_namespaced_pod_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_put_namespaced_pod_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_post_namespaced_pod_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_delete_namespaced_pod_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_options_namespaced_pod_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_head_namespaced_pod_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_patch_namespaced_pod_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def read_namespaced_pod_status(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1Pod: ...
    async def replace_namespaced_pod_status(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1Pod,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Pod: ...
    async def patch_namespaced_pod_status(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1Pod: ...
    async def list_namespaced_pod_template(
        self,
        namespace: str,
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
    ) -> kubernetes_asyncio.client.V1PodTemplateList: ...
    async def create_namespaced_pod_template(
        self,
        namespace: str,
        body: kubernetes_asyncio.client.V1PodTemplate,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1PodTemplate: ...
    async def delete_collection_namespaced_pod_template(
        self,
        namespace: str,
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
    async def read_namespaced_pod_template(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1PodTemplate: ...
    async def replace_namespaced_pod_template(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1PodTemplate,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1PodTemplate: ...
    async def delete_namespaced_pod_template(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1PodTemplate: ...
    async def patch_namespaced_pod_template(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1PodTemplate: ...
    async def list_namespaced_replication_controller(
        self,
        namespace: str,
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
    ) -> kubernetes_asyncio.client.V1ReplicationControllerList: ...
    async def create_namespaced_replication_controller(
        self,
        namespace: str,
        body: kubernetes_asyncio.client.V1ReplicationController,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1ReplicationController: ...
    async def delete_collection_namespaced_replication_controller(
        self,
        namespace: str,
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
    async def read_namespaced_replication_controller(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1ReplicationController: ...
    async def replace_namespaced_replication_controller(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1ReplicationController,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1ReplicationController: ...
    async def delete_namespaced_replication_controller(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Status: ...
    async def patch_namespaced_replication_controller(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1ReplicationController: ...
    async def read_namespaced_replication_controller_scale(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1Scale: ...
    async def replace_namespaced_replication_controller_scale(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1Scale,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Scale: ...
    async def patch_namespaced_replication_controller_scale(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1Scale: ...
    async def read_namespaced_replication_controller_status(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1ReplicationController: ...
    async def replace_namespaced_replication_controller_status(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1ReplicationController,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1ReplicationController: ...
    async def patch_namespaced_replication_controller_status(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1ReplicationController: ...
    async def list_namespaced_resource_quota(
        self,
        namespace: str,
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
    ) -> kubernetes_asyncio.client.V1ResourceQuotaList: ...
    async def create_namespaced_resource_quota(
        self,
        namespace: str,
        body: kubernetes_asyncio.client.V1ResourceQuota,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1ResourceQuota: ...
    async def delete_collection_namespaced_resource_quota(
        self,
        namespace: str,
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
    async def read_namespaced_resource_quota(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1ResourceQuota: ...
    async def replace_namespaced_resource_quota(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1ResourceQuota,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1ResourceQuota: ...
    async def delete_namespaced_resource_quota(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1ResourceQuota: ...
    async def patch_namespaced_resource_quota(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1ResourceQuota: ...
    async def read_namespaced_resource_quota_status(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1ResourceQuota: ...
    async def replace_namespaced_resource_quota_status(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1ResourceQuota,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1ResourceQuota: ...
    async def patch_namespaced_resource_quota_status(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1ResourceQuota: ...
    async def list_namespaced_secret(
        self,
        namespace: str,
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
    ) -> kubernetes_asyncio.client.V1SecretList: ...
    async def create_namespaced_secret(
        self,
        namespace: str,
        body: kubernetes_asyncio.client.V1Secret,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Secret: ...
    async def delete_collection_namespaced_secret(
        self,
        namespace: str,
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
    async def read_namespaced_secret(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1Secret: ...
    async def replace_namespaced_secret(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1Secret,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Secret: ...
    async def delete_namespaced_secret(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Status: ...
    async def patch_namespaced_secret(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1Secret: ...
    async def list_namespaced_service_account(
        self,
        namespace: str,
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
    ) -> kubernetes_asyncio.client.V1ServiceAccountList: ...
    async def create_namespaced_service_account(
        self,
        namespace: str,
        body: kubernetes_asyncio.client.V1ServiceAccount,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1ServiceAccount: ...
    async def delete_collection_namespaced_service_account(
        self,
        namespace: str,
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
    async def read_namespaced_service_account(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1ServiceAccount: ...
    async def replace_namespaced_service_account(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1ServiceAccount,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1ServiceAccount: ...
    async def delete_namespaced_service_account(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1ServiceAccount: ...
    async def patch_namespaced_service_account(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1ServiceAccount: ...
    async def create_namespaced_service_account_token(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.AuthenticationV1TokenRequest,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.AuthenticationV1TokenRequest: ...
    async def list_namespaced_service(
        self,
        namespace: str,
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
    ) -> kubernetes_asyncio.client.V1ServiceList: ...
    async def create_namespaced_service(
        self,
        namespace: str,
        body: kubernetes_asyncio.client.V1Service,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Service: ...
    async def delete_collection_namespaced_service(
        self,
        namespace: str,
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
    async def read_namespaced_service(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1Service: ...
    async def replace_namespaced_service(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1Service,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Service: ...
    async def delete_namespaced_service(
        self,
        name: str,
        namespace: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Service: ...
    async def patch_namespaced_service(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1Service: ...
    async def connect_get_namespaced_service_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_put_namespaced_service_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_post_namespaced_service_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_delete_namespaced_service_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_options_namespaced_service_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_head_namespaced_service_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_patch_namespaced_service_proxy(
        self, name: str, namespace: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_get_namespaced_service_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_put_namespaced_service_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_post_namespaced_service_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_delete_namespaced_service_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_options_namespaced_service_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_head_namespaced_service_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_patch_namespaced_service_proxy_with_path(
        self, name: str, namespace: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def read_namespaced_service_status(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1Service: ...
    async def replace_namespaced_service_status(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1Service,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Service: ...
    async def patch_namespaced_service_status(
        self,
        name: str,
        namespace: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1Service: ...
    async def read_namespace(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1Namespace: ...
    async def replace_namespace(
        self,
        name: str,
        body: kubernetes_asyncio.client.V1Namespace,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Namespace: ...
    async def delete_namespace(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Status: ...
    async def patch_namespace(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1Namespace: ...
    async def replace_namespace_finalize(
        self,
        name: str,
        body: kubernetes_asyncio.client.V1Namespace,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Namespace: ...
    async def read_namespace_status(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1Namespace: ...
    async def replace_namespace_status(
        self,
        name: str,
        body: kubernetes_asyncio.client.V1Namespace,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Namespace: ...
    async def patch_namespace_status(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1Namespace: ...
    async def list_node(
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
    ) -> kubernetes_asyncio.client.V1NodeList: ...
    async def create_node(
        self,
        body: kubernetes_asyncio.client.V1Node,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Node: ...
    async def delete_collection_node(
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
    async def read_node(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1Node: ...
    async def replace_node(
        self,
        name: str,
        body: kubernetes_asyncio.client.V1Node,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Node: ...
    async def delete_node(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Status: ...
    async def patch_node(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1Node: ...
    async def connect_get_node_proxy(
        self, name: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_put_node_proxy(
        self, name: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_post_node_proxy(
        self, name: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_delete_node_proxy(
        self, name: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_options_node_proxy(
        self, name: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_head_node_proxy(
        self, name: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_patch_node_proxy(
        self, name: str, *, path: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_get_node_proxy_with_path(
        self, name: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_put_node_proxy_with_path(
        self, name: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_post_node_proxy_with_path(
        self, name: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_delete_node_proxy_with_path(
        self, name: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_options_node_proxy_with_path(
        self, name: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_head_node_proxy_with_path(
        self, name: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def connect_patch_node_proxy_with_path(
        self, name: str, path: str, *, path2: typing.Optional[str] = ...
    ) -> str: ...
    async def read_node_status(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1Node: ...
    async def replace_node_status(
        self,
        name: str,
        body: kubernetes_asyncio.client.V1Node,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Node: ...
    async def patch_node_status(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1Node: ...
    async def list_persistent_volume_claim_for_all_namespaces(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        pretty: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1PersistentVolumeClaimList: ...
    async def list_persistent_volume(
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
    ) -> kubernetes_asyncio.client.V1PersistentVolumeList: ...
    async def create_persistent_volume(
        self,
        body: kubernetes_asyncio.client.V1PersistentVolume,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1PersistentVolume: ...
    async def delete_collection_persistent_volume(
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
    async def read_persistent_volume(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1PersistentVolume: ...
    async def replace_persistent_volume(
        self,
        name: str,
        body: kubernetes_asyncio.client.V1PersistentVolume,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1PersistentVolume: ...
    async def delete_persistent_volume(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1PersistentVolume: ...
    async def patch_persistent_volume(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1PersistentVolume: ...
    async def read_persistent_volume_status(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1PersistentVolume: ...
    async def replace_persistent_volume_status(
        self,
        name: str,
        body: kubernetes_asyncio.client.V1PersistentVolume,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1PersistentVolume: ...
    async def patch_persistent_volume_status(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1PersistentVolume: ...
    async def list_pod_for_all_namespaces(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        pretty: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1PodList: ...
    async def list_pod_template_for_all_namespaces(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        pretty: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1PodTemplateList: ...
    async def list_replication_controller_for_all_namespaces(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        pretty: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1ReplicationControllerList: ...
    async def list_resource_quota_for_all_namespaces(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        pretty: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1ResourceQuotaList: ...
    async def list_secret_for_all_namespaces(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        pretty: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1SecretList: ...
    async def list_service_account_for_all_namespaces(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        pretty: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1ServiceAccountList: ...
    async def list_service_for_all_namespaces(
        self,
        *,
        allow_watch_bookmarks: typing.Optional[bool] = ...,
        _continue: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        pretty: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
        watch: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1ServiceList: ...
