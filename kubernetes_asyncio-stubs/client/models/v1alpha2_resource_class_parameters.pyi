import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha2ResourceClassParameters:
    api_version: str
    filters: typing.Optional[list[kubernetes_asyncio.client.V1alpha2ResourceFilter]]
    generated_from: typing.Optional[
        kubernetes_asyncio.client.V1alpha2ResourceClassParametersReference
    ]
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    vendor_parameters: typing.Optional[
        list[kubernetes_asyncio.client.V1alpha2VendorParameters]
    ]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        filters: typing.Optional[
            list[kubernetes_asyncio.client.V1alpha2ResourceFilter]
        ] = ...,
        generated_from: typing.Optional[
            kubernetes_asyncio.client.V1alpha2ResourceClassParametersReference
        ] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        vendor_parameters: typing.Optional[
            list[kubernetes_asyncio.client.V1alpha2VendorParameters]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2ResourceClassParametersDict: ...

class V1alpha2ResourceClassParametersDict(typing.TypedDict, total=False):
    apiVersion: str
    filters: list[kubernetes_asyncio.client.V1alpha2ResourceFilterDict]
    generatedFrom: (
        kubernetes_asyncio.client.V1alpha2ResourceClassParametersReferenceDict
    )
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    vendorParameters: list[kubernetes_asyncio.client.V1alpha2VendorParametersDict]
