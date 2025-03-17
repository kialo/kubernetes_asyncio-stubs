import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha3DeviceClassSpec:
    config: typing.Optional[
        list[kubernetes_asyncio.client.V1alpha3DeviceClassConfiguration]
    ]
    selectors: typing.Optional[list[kubernetes_asyncio.client.V1alpha3DeviceSelector]]
    suitable_nodes: typing.Optional[kubernetes_asyncio.client.V1NodeSelector]

    def __init__(
        self,
        *,
        config: typing.Optional[
            list[kubernetes_asyncio.client.V1alpha3DeviceClassConfiguration]
        ] = ...,
        selectors: typing.Optional[
            list[kubernetes_asyncio.client.V1alpha3DeviceSelector]
        ] = ...,
        suitable_nodes: typing.Optional[kubernetes_asyncio.client.V1NodeSelector] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha3DeviceClassSpecDict: ...

class V1alpha3DeviceClassSpecDict(typing.TypedDict, total=False):
    config: list[kubernetes_asyncio.client.V1alpha3DeviceClassConfigurationDict]
    selectors: list[kubernetes_asyncio.client.V1alpha3DeviceSelectorDict]
    suitableNodes: kubernetes_asyncio.client.V1NodeSelectorDict
