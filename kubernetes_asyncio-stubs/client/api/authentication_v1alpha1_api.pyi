import kubernetes_asyncio.client
import typing

class AuthenticationV1alpha1Api:
    def __init__(
        self,
        api_client: typing.Optional[
            kubernetes_asyncio.client.api_client.ApiClient
        ] = ...,
    ) -> None: ...
    async def get_api_resources(
        self,
    ) -> kubernetes_asyncio.client.V1APIResourceList: ...
    async def create_self_subject_review(
        self,
        body: kubernetes_asyncio.client.V1alpha1SelfSubjectReview,
        *,
        dry_run: typing.Optional[str] = ...,
        field_manager: typing.Optional[str] = ...,
        field_validation: typing.Optional[str] = ...,
        pretty: typing.Optional[str] = ...,
    ) -> kubernetes_asyncio.client.V1alpha1SelfSubjectReview: ...
