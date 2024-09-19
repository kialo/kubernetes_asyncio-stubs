import kubernetes_asyncio.client
import typing

class PolicyV1Api:
    def __init__(
        self,
        api_client: typing.Optional[
            kubernetes_asyncio.client.api_client.ApiClient
        ] = ...,
    ) -> None: ...
    async def get_api_resources(
        self,
    ) -> kubernetes_asyncio.client.V1APIResourceList: ...
    async def list_namespaced_pod_disruption_budget(
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
    ) -> kubernetes_asyncio.client.V1PodDisruptionBudgetList: ...
    async def create_namespaced_pod_disruption_budget(
        self,
        namespace: str,
        body: kubernetes_asyncio.client.V1PodDisruptionBudget,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1PodDisruptionBudget: ...
    async def delete_collection_namespaced_pod_disruption_budget(
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
    async def read_namespaced_pod_disruption_budget(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1PodDisruptionBudget: ...
    async def replace_namespaced_pod_disruption_budget(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1PodDisruptionBudget,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1PodDisruptionBudget: ...
    async def delete_namespaced_pod_disruption_budget(
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
    async def patch_namespaced_pod_disruption_budget(
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
    ) -> kubernetes_asyncio.client.V1PodDisruptionBudget: ...
    async def read_namespaced_pod_disruption_budget_status(
        self, name: str, namespace: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1PodDisruptionBudget: ...
    async def replace_namespaced_pod_disruption_budget_status(
        self,
        name: str,
        namespace: str,
        body: kubernetes_asyncio.client.V1PodDisruptionBudget,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1PodDisruptionBudget: ...
    async def patch_namespaced_pod_disruption_budget_status(
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
    ) -> kubernetes_asyncio.client.V1PodDisruptionBudget: ...
    async def list_pod_disruption_budget_for_all_namespaces(
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
    ) -> kubernetes_asyncio.client.V1PodDisruptionBudgetList: ...
