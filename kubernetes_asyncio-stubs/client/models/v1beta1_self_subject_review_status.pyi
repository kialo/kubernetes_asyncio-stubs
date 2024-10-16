import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1SelfSubjectReviewStatus:
    user_info: typing.Optional[kubernetes_asyncio.client.V1UserInfo]

    def __init__(
        self, *, user_info: typing.Optional[kubernetes_asyncio.client.V1UserInfo] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1SelfSubjectReviewStatusDict: ...

class V1beta1SelfSubjectReviewStatusDict(typing.TypedDict, total=False):
    userInfo: kubernetes_asyncio.client.V1UserInfoDict
