import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha2ResourceFilter:
    driver_name: typing.Optional[str]
    named_resources: typing.Optional[
        kubernetes_asyncio.client.V1alpha2NamedResourcesFilter
    ]

    def __init__(
        self,
        *,
        driver_name: typing.Optional[str] = ...,
        named_resources: typing.Optional[
            kubernetes_asyncio.client.V1alpha2NamedResourcesFilter
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2ResourceFilterDict: ...

class V1alpha2ResourceFilterDict(typing.TypedDict, total=False):
    driverName: str
    namedResources: kubernetes_asyncio.client.V1alpha2NamedResourcesFilterDict
