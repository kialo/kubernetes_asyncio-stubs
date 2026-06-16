import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1DeviceCapacity:
    request_policy: typing.Optional[kubernetes_asyncio.client.V1CapacityRequestPolicy]
    value: str

    def __init__(
        self,
        *,
        request_policy: typing.Optional[
            kubernetes_asyncio.client.V1CapacityRequestPolicy
        ] = ...,
        value: str,
    ) -> None: ...
    def to_dict(self) -> V1DeviceCapacityDict: ...

class V1DeviceCapacityDict(typing.TypedDict, total=False):
    requestPolicy: kubernetes_asyncio.client.V1CapacityRequestPolicyDict
    value: str
