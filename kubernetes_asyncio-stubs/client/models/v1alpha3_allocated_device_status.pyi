import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha3AllocatedDeviceStatus:
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1Condition]]
    data: typing.Optional[typing.Any]
    device: str
    driver: str
    network_data: typing.Optional[kubernetes_asyncio.client.V1alpha3NetworkDeviceData]
    pool: str

    def __init__(
        self,
        *,
        conditions: typing.Optional[list[kubernetes_asyncio.client.V1Condition]] = ...,
        data: typing.Optional[typing.Any] = ...,
        device: str,
        driver: str,
        network_data: typing.Optional[
            kubernetes_asyncio.client.V1alpha3NetworkDeviceData
        ] = ...,
        pool: str,
    ) -> None: ...
    def to_dict(self) -> V1alpha3AllocatedDeviceStatusDict: ...

class V1alpha3AllocatedDeviceStatusDict(typing.TypedDict, total=False):
    conditions: list[kubernetes_asyncio.client.V1ConditionDict]
    data: typing.Any
    device: str
    driver: str
    networkData: kubernetes_asyncio.client.V1alpha3NetworkDeviceDataDict
    pool: str
