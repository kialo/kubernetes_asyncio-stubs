import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PodFailurePolicyRule:
    action: str
    on_exit_codes: typing.Optional[
        kubernetes_asyncio.client.V1PodFailurePolicyOnExitCodesRequirement
    ]
    on_pod_conditions: typing.Optional[
        list[kubernetes_asyncio.client.V1PodFailurePolicyOnPodConditionsPattern]
    ]

    def __init__(
        self,
        *,
        action: str,
        on_exit_codes: typing.Optional[
            kubernetes_asyncio.client.V1PodFailurePolicyOnExitCodesRequirement
        ] = ...,
        on_pod_conditions: typing.Optional[
            list[kubernetes_asyncio.client.V1PodFailurePolicyOnPodConditionsPattern]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PodFailurePolicyRuleDict: ...

class V1PodFailurePolicyRuleDict(typing.TypedDict, total=False):
    action: str
    onExitCodes: kubernetes_asyncio.client.V1PodFailurePolicyOnExitCodesRequirementDict
    onPodConditions: list[
        kubernetes_asyncio.client.V1PodFailurePolicyOnPodConditionsPatternDict
    ]
