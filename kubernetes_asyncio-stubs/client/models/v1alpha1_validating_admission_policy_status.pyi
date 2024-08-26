import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1ValidatingAdmissionPolicyStatus:
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1Condition]]
    observed_generation: typing.Optional[int]
    type_checking: typing.Optional[kubernetes_asyncio.client.V1alpha1TypeChecking]

    def __init__(
        self,
        *,
        conditions: typing.Optional[list[kubernetes_asyncio.client.V1Condition]] = ...,
        observed_generation: typing.Optional[int] = ...,
        type_checking: typing.Optional[
            kubernetes_asyncio.client.V1alpha1TypeChecking
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1ValidatingAdmissionPolicyStatusDict: ...

class V1alpha1ValidatingAdmissionPolicyStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1ConditionDict]]
    observedGeneration: typing.Optional[int]
    typeChecking: typing.Optional[kubernetes_asyncio.client.V1alpha1TypeCheckingDict]
