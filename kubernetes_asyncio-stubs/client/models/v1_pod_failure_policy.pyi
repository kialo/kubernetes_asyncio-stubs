import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PodFailurePolicy:
    rules: list[kubernetes_asyncio.client.V1PodFailurePolicyRule]

    def __init__(
        self, *, rules: list[kubernetes_asyncio.client.V1PodFailurePolicyRule]
    ) -> None: ...
    def to_dict(self) -> V1PodFailurePolicyDict: ...

class V1PodFailurePolicyDict(typing.TypedDict, total=False):
    rules: list[kubernetes_asyncio.client.V1PodFailurePolicyRuleDict]
