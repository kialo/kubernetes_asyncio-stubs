import kubernetes_asyncio.client
import typing

class AuthorizationV1Api:
    def __init__(
        self,
        api_client: typing.Optional[
            kubernetes_asyncio.client.api_client.ApiClient
        ] = ...,
    ) -> None: ...
    async def get_api_resources(
        self,
    ) -> kubernetes_asyncio.client.V1APIResourceList: ...
    async def create_namespaced_local_subject_access_review(
        self,
        namespace: str,
        body: kubernetes_asyncio.client.V1LocalSubjectAccessReview,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1LocalSubjectAccessReview: ...
    async def create_self_subject_access_review(
        self,
        body: kubernetes_asyncio.client.V1SelfSubjectAccessReview,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1SelfSubjectAccessReview: ...
    async def create_self_subject_rules_review(
        self,
        body: kubernetes_asyncio.client.V1SelfSubjectRulesReview,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1SelfSubjectRulesReview: ...
    async def create_subject_access_review(
        self,
        body: kubernetes_asyncio.client.V1SubjectAccessReview,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1SubjectAccessReview: ...
