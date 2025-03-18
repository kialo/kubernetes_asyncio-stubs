import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PodDisruptionBudgetStatus:
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1Condition]]
    current_healthy: int
    desired_healthy: int
    disrupted_pods: typing.Optional[dict[str, datetime.datetime]]
    disruptions_allowed: int
    expected_pods: int
    observed_generation: typing.Optional[int]

    def __init__(
        self,
        *,
        conditions: typing.Optional[list[kubernetes_asyncio.client.V1Condition]] = ...,
        current_healthy: int,
        desired_healthy: int,
        disrupted_pods: typing.Optional[dict[str, datetime.datetime]] = ...,
        disruptions_allowed: int,
        expected_pods: int,
        observed_generation: typing.Optional[int] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PodDisruptionBudgetStatusDict: ...

class V1PodDisruptionBudgetStatusDict(typing.TypedDict, total=False):
    conditions: list[kubernetes_asyncio.client.V1ConditionDict]
    currentHealthy: int
    desiredHealthy: int
    disruptedPods: dict[str, datetime.datetime]
    disruptionsAllowed: int
    expectedPods: int
    observedGeneration: int
