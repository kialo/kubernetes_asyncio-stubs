import kubernetes_asyncio.client
import typing

class AdmissionregistrationV1Api:
    def __init__(
        self,
        api_client: typing.Optional[
            kubernetes_asyncio.client.api_client.ApiClient
        ] = ...,
    ) -> None: ...
    async def get_api_resources(
        self,
    ) -> kubernetes_asyncio.client.V1APIResourceList: ...
    async def list_mutating_webhook_configuration(
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
    ) -> kubernetes_asyncio.client.V1MutatingWebhookConfigurationList: ...
    async def create_mutating_webhook_configuration(
        self,
        body: kubernetes_asyncio.client.V1MutatingWebhookConfiguration,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1MutatingWebhookConfiguration: ...
    async def delete_collection_mutating_webhook_configuration(
        self,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        _continue: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        ignore_store_read_error_with_cluster_breaking_potential: typing.Optional[
            bool
        ] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
    ) -> kubernetes_asyncio.client.V1Status: ...
    async def read_mutating_webhook_configuration(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1MutatingWebhookConfiguration: ...
    async def replace_mutating_webhook_configuration(
        self,
        name: str,
        body: kubernetes_asyncio.client.V1MutatingWebhookConfiguration,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1MutatingWebhookConfiguration: ...
    async def delete_mutating_webhook_configuration(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        ignore_store_read_error_with_cluster_breaking_potential: typing.Optional[
            bool
        ] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Status: ...
    async def patch_mutating_webhook_configuration(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1MutatingWebhookConfiguration: ...
    async def list_validating_admission_policy(
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
    ) -> kubernetes_asyncio.client.V1ValidatingAdmissionPolicyList: ...
    async def create_validating_admission_policy(
        self,
        body: kubernetes_asyncio.client.V1ValidatingAdmissionPolicy,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1ValidatingAdmissionPolicy: ...
    async def delete_collection_validating_admission_policy(
        self,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        _continue: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        ignore_store_read_error_with_cluster_breaking_potential: typing.Optional[
            bool
        ] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
    ) -> kubernetes_asyncio.client.V1Status: ...
    async def read_validating_admission_policy(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1ValidatingAdmissionPolicy: ...
    async def replace_validating_admission_policy(
        self,
        name: str,
        body: kubernetes_asyncio.client.V1ValidatingAdmissionPolicy,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1ValidatingAdmissionPolicy: ...
    async def delete_validating_admission_policy(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        ignore_store_read_error_with_cluster_breaking_potential: typing.Optional[
            bool
        ] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Status: ...
    async def patch_validating_admission_policy(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1ValidatingAdmissionPolicy: ...
    async def read_validating_admission_policy_status(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1ValidatingAdmissionPolicy: ...
    async def replace_validating_admission_policy_status(
        self,
        name: str,
        body: kubernetes_asyncio.client.V1ValidatingAdmissionPolicy,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1ValidatingAdmissionPolicy: ...
    async def patch_validating_admission_policy_status(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1ValidatingAdmissionPolicy: ...
    async def list_validating_admission_policy_binding(
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
    ) -> kubernetes_asyncio.client.V1ValidatingAdmissionPolicyBindingList: ...
    async def create_validating_admission_policy_binding(
        self,
        body: kubernetes_asyncio.client.V1ValidatingAdmissionPolicyBinding,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1ValidatingAdmissionPolicyBinding: ...
    async def delete_collection_validating_admission_policy_binding(
        self,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        _continue: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        ignore_store_read_error_with_cluster_breaking_potential: typing.Optional[
            bool
        ] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
    ) -> kubernetes_asyncio.client.V1Status: ...
    async def read_validating_admission_policy_binding(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1ValidatingAdmissionPolicyBinding: ...
    async def replace_validating_admission_policy_binding(
        self,
        name: str,
        body: kubernetes_asyncio.client.V1ValidatingAdmissionPolicyBinding,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1ValidatingAdmissionPolicyBinding: ...
    async def delete_validating_admission_policy_binding(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        ignore_store_read_error_with_cluster_breaking_potential: typing.Optional[
            bool
        ] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Status: ...
    async def patch_validating_admission_policy_binding(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1ValidatingAdmissionPolicyBinding: ...
    async def list_validating_webhook_configuration(
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
    ) -> kubernetes_asyncio.client.V1ValidatingWebhookConfigurationList: ...
    async def create_validating_webhook_configuration(
        self,
        body: kubernetes_asyncio.client.V1ValidatingWebhookConfiguration,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1ValidatingWebhookConfiguration: ...
    async def delete_collection_validating_webhook_configuration(
        self,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        _continue: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_selector: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        ignore_store_read_error_with_cluster_breaking_potential: typing.Optional[
            bool
        ] = ...,
        label_selector: typing.Optional[str] = ...,
        limit: typing.Optional[int] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
        resource_version: typing.Optional[str] = ...,
        resource_version_match: typing.Optional[str] = ...,
        send_initial_events: typing.Optional[bool] = ...,
        timeout_seconds: typing.Optional[int] = ...,
    ) -> kubernetes_asyncio.client.V1Status: ...
    async def read_validating_webhook_configuration(
        self, name: str, *, pretty: typing.Optional[str] = ...
    ) -> kubernetes_asyncio.client.V1ValidatingWebhookConfiguration: ...
    async def replace_validating_webhook_configuration(
        self,
        name: str,
        body: kubernetes_asyncio.client.V1ValidatingWebhookConfiguration,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1ValidatingWebhookConfiguration: ...
    async def delete_validating_webhook_configuration(
        self,
        name: str,
        *,
        pretty: typing.Optional[str] = ...,
        body: typing.Optional[kubernetes_asyncio.client.V1DeleteOptions] = ...,
        dry_run: typing.Optional[str] = ...,
        grace_period_seconds: typing.Optional[int] = ...,
        ignore_store_read_error_with_cluster_breaking_potential: typing.Optional[
            bool
        ] = ...,
        orphan_dependents: typing.Optional[bool] = ...,
        propagation_policy: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1Status: ...
    async def patch_validating_webhook_configuration(
        self,
        name: str,
        body: typing.Any,
        *,
        pretty: typing.Optional[str] = ...,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        force: typing.Optional[bool] = ...,
    ) -> kubernetes_asyncio.client.V1ValidatingWebhookConfiguration: ...
