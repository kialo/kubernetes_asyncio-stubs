import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1SuccessPolicy:
    rules: list[kubernetes_asyncio.client.V1SuccessPolicyRule]

    def __init__(
        self, *, rules: list[kubernetes_asyncio.client.V1SuccessPolicyRule]
    ) -> None: ...
    def to_dict(self) -> V1SuccessPolicyDict: ...

class V1SuccessPolicyDict(typing.TypedDict, total=False):
    rules: list[kubernetes_asyncio.client.V1SuccessPolicyRuleDict]
