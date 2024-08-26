import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1SelfSubjectReviewStatus:
    user_info: typing.Optional[kubernetes_asyncio.client.V1UserInfo]

    def __init__(
        self, *, user_info: typing.Optional[kubernetes_asyncio.client.V1UserInfo] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1SelfSubjectReviewStatusDict: ...

class V1alpha1SelfSubjectReviewStatusDict(typing.TypedDict, total=False):
    userInfo: typing.Optional[kubernetes_asyncio.client.V1UserInfoDict]
