import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V2HPAScalingRules:
    policies: typing.Optional[list[kubernetes_asyncio.client.V2HPAScalingPolicy]]
    select_policy: typing.Optional[str]
    stabilization_window_seconds: typing.Optional[int]
    tolerance: typing.Optional[str]

    def __init__(
        self,
        *,
        policies: typing.Optional[
            list[kubernetes_asyncio.client.V2HPAScalingPolicy]
        ] = ...,
        select_policy: typing.Optional[str] = ...,
        stabilization_window_seconds: typing.Optional[int] = ...,
        tolerance: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V2HPAScalingRulesDict: ...

class V2HPAScalingRulesDict(typing.TypedDict, total=False):
    policies: list[kubernetes_asyncio.client.V2HPAScalingPolicyDict]
    selectPolicy: str
    stabilizationWindowSeconds: int
    tolerance: str
