import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1SelfSubjectReview:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    status: typing.Optional[kubernetes_asyncio.client.V1alpha1SelfSubjectReviewStatus]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        status: typing.Optional[
            kubernetes_asyncio.client.V1alpha1SelfSubjectReviewStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1SelfSubjectReviewDict: ...

class V1alpha1SelfSubjectReviewDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    status: typing.Optional[
        kubernetes_asyncio.client.V1alpha1SelfSubjectReviewStatusDict
    ]
