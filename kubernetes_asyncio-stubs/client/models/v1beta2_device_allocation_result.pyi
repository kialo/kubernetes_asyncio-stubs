import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2DeviceAllocationResult:
    config: typing.Optional[
        list[kubernetes_asyncio.client.V1beta2DeviceAllocationConfiguration]
    ]
    results: typing.Optional[
        list[kubernetes_asyncio.client.V1beta2DeviceRequestAllocationResult]
    ]

    def __init__(
        self,
        *,
        config: typing.Optional[
            list[kubernetes_asyncio.client.V1beta2DeviceAllocationConfiguration]
        ] = ...,
        results: typing.Optional[
            list[kubernetes_asyncio.client.V1beta2DeviceRequestAllocationResult]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta2DeviceAllocationResultDict: ...

class V1beta2DeviceAllocationResultDict(typing.TypedDict, total=False):
    config: list[kubernetes_asyncio.client.V1beta2DeviceAllocationConfigurationDict]
    results: list[kubernetes_asyncio.client.V1beta2DeviceRequestAllocationResultDict]
