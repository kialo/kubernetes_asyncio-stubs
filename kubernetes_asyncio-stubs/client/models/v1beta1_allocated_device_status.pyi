import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1AllocatedDeviceStatus:
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1Condition]]
    data: typing.Optional[typing.Any]
    device: str
    driver: str
    network_data: typing.Optional[kubernetes_asyncio.client.V1beta1NetworkDeviceData]
    pool: str

    def __init__(
        self,
        *,
        conditions: typing.Optional[list[kubernetes_asyncio.client.V1Condition]] = ...,
        data: typing.Optional[typing.Any] = ...,
        device: str,
        driver: str,
        network_data: typing.Optional[
            kubernetes_asyncio.client.V1beta1NetworkDeviceData
        ] = ...,
        pool: str,
    ) -> None: ...
    def to_dict(self) -> V1beta1AllocatedDeviceStatusDict: ...

class V1beta1AllocatedDeviceStatusDict(typing.TypedDict, total=False):
    conditions: list[kubernetes_asyncio.client.V1ConditionDict]
    data: typing.Any
    device: str
    driver: str
    networkData: kubernetes_asyncio.client.V1beta1NetworkDeviceDataDict
    pool: str
