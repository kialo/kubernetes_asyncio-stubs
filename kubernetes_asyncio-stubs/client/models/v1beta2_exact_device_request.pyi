import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2ExactDeviceRequest:
    admin_access: typing.Optional[bool]
    allocation_mode: typing.Optional[str]
    count: typing.Optional[int]
    device_class_name: str
    selectors: typing.Optional[list[kubernetes_asyncio.client.V1beta2DeviceSelector]]
    tolerations: typing.Optional[
        list[kubernetes_asyncio.client.V1beta2DeviceToleration]
    ]

    def __init__(
        self,
        *,
        admin_access: typing.Optional[bool] = ...,
        allocation_mode: typing.Optional[str] = ...,
        count: typing.Optional[int] = ...,
        device_class_name: str,
        selectors: typing.Optional[
            list[kubernetes_asyncio.client.V1beta2DeviceSelector]
        ] = ...,
        tolerations: typing.Optional[
            list[kubernetes_asyncio.client.V1beta2DeviceToleration]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta2ExactDeviceRequestDict: ...

class V1beta2ExactDeviceRequestDict(typing.TypedDict, total=False):
    adminAccess: bool
    allocationMode: str
    count: int
    deviceClassName: str
    selectors: list[kubernetes_asyncio.client.V1beta2DeviceSelectorDict]
    tolerations: list[kubernetes_asyncio.client.V1beta2DeviceTolerationDict]
