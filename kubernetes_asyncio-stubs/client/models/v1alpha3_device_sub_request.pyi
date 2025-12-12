import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha3DeviceSubRequest:
    allocation_mode: typing.Optional[str]
    count: typing.Optional[int]
    device_class_name: str
    name: str
    selectors: typing.Optional[list[kubernetes_asyncio.client.V1alpha3DeviceSelector]]
    tolerations: typing.Optional[
        list[kubernetes_asyncio.client.V1alpha3DeviceToleration]
    ]

    def __init__(
        self,
        *,
        allocation_mode: typing.Optional[str] = ...,
        count: typing.Optional[int] = ...,
        device_class_name: str,
        name: str,
        selectors: typing.Optional[
            list[kubernetes_asyncio.client.V1alpha3DeviceSelector]
        ] = ...,
        tolerations: typing.Optional[
            list[kubernetes_asyncio.client.V1alpha3DeviceToleration]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3DeviceSubRequestDict: ...

class V1alpha3DeviceSubRequestDict(typing.TypedDict, total=False):
    allocationMode: str
    count: int
    deviceClassName: str
    name: str
    selectors: list[kubernetes_asyncio.client.V1alpha3DeviceSelectorDict]
    tolerations: list[kubernetes_asyncio.client.V1alpha3DeviceTolerationDict]
