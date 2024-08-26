import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha2ResourceHandle:
    data: typing.Optional[str]
    driver_name: typing.Optional[str]
    structured_data: typing.Optional[
        kubernetes_asyncio.client.V1alpha2StructuredResourceHandle
    ]

    def __init__(
        self,
        *,
        data: typing.Optional[str] = ...,
        driver_name: typing.Optional[str] = ...,
        structured_data: typing.Optional[
            kubernetes_asyncio.client.V1alpha2StructuredResourceHandle
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2ResourceHandleDict: ...

class V1alpha2ResourceHandleDict(typing.TypedDict, total=False):
    data: typing.Optional[str]
    driverName: typing.Optional[str]
    structuredData: typing.Optional[
        kubernetes_asyncio.client.V1alpha2StructuredResourceHandleDict
    ]
