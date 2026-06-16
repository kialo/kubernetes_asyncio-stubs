import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1CapacityRequestPolicy:
    default: typing.Optional[str]
    valid_range: typing.Optional[
        kubernetes_asyncio.client.V1beta1CapacityRequestPolicyRange
    ]
    valid_values: typing.Optional[list[str]]

    def __init__(
        self,
        *,
        default: typing.Optional[str] = ...,
        valid_range: typing.Optional[
            kubernetes_asyncio.client.V1beta1CapacityRequestPolicyRange
        ] = ...,
        valid_values: typing.Optional[list[str]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1CapacityRequestPolicyDict: ...

class V1beta1CapacityRequestPolicyDict(typing.TypedDict, total=False):
    default: str
    validRange: kubernetes_asyncio.client.V1beta1CapacityRequestPolicyRangeDict
    validValues: list[str]
