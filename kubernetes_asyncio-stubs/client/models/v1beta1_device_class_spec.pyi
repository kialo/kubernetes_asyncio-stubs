import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1DeviceClassSpec:
    config: typing.Optional[
        list[kubernetes_asyncio.client.V1beta1DeviceClassConfiguration]
    ]
    selectors: typing.Optional[list[kubernetes_asyncio.client.V1beta1DeviceSelector]]

    def __init__(
        self,
        *,
        config: typing.Optional[
            list[kubernetes_asyncio.client.V1beta1DeviceClassConfiguration]
        ] = ...,
        selectors: typing.Optional[
            list[kubernetes_asyncio.client.V1beta1DeviceSelector]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1DeviceClassSpecDict: ...

class V1beta1DeviceClassSpecDict(typing.TypedDict, total=False):
    config: list[kubernetes_asyncio.client.V1beta1DeviceClassConfigurationDict]
    selectors: list[kubernetes_asyncio.client.V1beta1DeviceSelectorDict]
