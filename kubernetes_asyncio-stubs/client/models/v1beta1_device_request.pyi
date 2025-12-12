import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1DeviceRequest:
    admin_access: typing.Optional[bool]
    allocation_mode: typing.Optional[str]
    count: typing.Optional[int]
    device_class_name: typing.Optional[str]
    first_available: typing.Optional[
        list[kubernetes_asyncio.client.V1beta1DeviceSubRequest]
    ]
    name: str
    selectors: typing.Optional[list[kubernetes_asyncio.client.V1beta1DeviceSelector]]
    tolerations: typing.Optional[
        list[kubernetes_asyncio.client.V1beta1DeviceToleration]
    ]

    def __init__(
        self,
        *,
        admin_access: typing.Optional[bool] = ...,
        allocation_mode: typing.Optional[str] = ...,
        count: typing.Optional[int] = ...,
        device_class_name: typing.Optional[str] = ...,
        first_available: typing.Optional[
            list[kubernetes_asyncio.client.V1beta1DeviceSubRequest]
        ] = ...,
        name: str,
        selectors: typing.Optional[
            list[kubernetes_asyncio.client.V1beta1DeviceSelector]
        ] = ...,
        tolerations: typing.Optional[
            list[kubernetes_asyncio.client.V1beta1DeviceToleration]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1DeviceRequestDict: ...

class V1beta1DeviceRequestDict(typing.TypedDict, total=False):
    adminAccess: bool
    allocationMode: str
    count: int
    deviceClassName: str
    firstAvailable: list[kubernetes_asyncio.client.V1beta1DeviceSubRequestDict]
    name: str
    selectors: list[kubernetes_asyncio.client.V1beta1DeviceSelectorDict]
    tolerations: list[kubernetes_asyncio.client.V1beta1DeviceTolerationDict]
