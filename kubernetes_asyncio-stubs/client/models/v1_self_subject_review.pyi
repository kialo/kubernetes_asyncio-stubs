import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1SelfSubjectReview:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    status: kubernetes_asyncio.client.V1SelfSubjectReviewStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        status: typing.Optional[
            kubernetes_asyncio.client.V1SelfSubjectReviewStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1SelfSubjectReviewDict: ...

class V1SelfSubjectReviewDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    status: kubernetes_asyncio.client.V1SelfSubjectReviewStatusDict
