import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1ValidatingAdmissionPolicyStatus:
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1Condition]]
    observed_generation: typing.Optional[int]
    type_checking: typing.Optional[kubernetes_asyncio.client.V1beta1TypeChecking]

    def __init__(
        self,
        *,
        conditions: typing.Optional[list[kubernetes_asyncio.client.V1Condition]] = ...,
        observed_generation: typing.Optional[int] = ...,
        type_checking: typing.Optional[
            kubernetes_asyncio.client.V1beta1TypeChecking
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1ValidatingAdmissionPolicyStatusDict: ...

class V1beta1ValidatingAdmissionPolicyStatusDict(typing.TypedDict, total=False):
    conditions: list[kubernetes_asyncio.client.V1ConditionDict]
    observedGeneration: int
    typeChecking: kubernetes_asyncio.client.V1beta1TypeCheckingDict
