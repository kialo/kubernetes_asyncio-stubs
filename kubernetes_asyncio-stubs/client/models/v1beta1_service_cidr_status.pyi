import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1ServiceCIDRStatus:
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1Condition]]

    def __init__(
        self,
        *,
        conditions: typing.Optional[list[kubernetes_asyncio.client.V1Condition]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1ServiceCIDRStatusDict: ...

class V1beta1ServiceCIDRStatusDict(typing.TypedDict, total=False):
    conditions: list[kubernetes_asyncio.client.V1ConditionDict]
