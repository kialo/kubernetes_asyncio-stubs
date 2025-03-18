import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha2ResourceClaimParameters:
    api_version: str
    driver_requests: typing.Optional[
        list[kubernetes_asyncio.client.V1alpha2DriverRequests]
    ]
    generated_from: typing.Optional[
        kubernetes_asyncio.client.V1alpha2ResourceClaimParametersReference
    ]
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    shareable: typing.Optional[bool]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        driver_requests: typing.Optional[
            list[kubernetes_asyncio.client.V1alpha2DriverRequests]
        ] = ...,
        generated_from: typing.Optional[
            kubernetes_asyncio.client.V1alpha2ResourceClaimParametersReference
        ] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        shareable: typing.Optional[bool] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2ResourceClaimParametersDict: ...

class V1alpha2ResourceClaimParametersDict(typing.TypedDict, total=False):
    apiVersion: str
    driverRequests: list[kubernetes_asyncio.client.V1alpha2DriverRequestsDict]
    generatedFrom: (
        kubernetes_asyncio.client.V1alpha2ResourceClaimParametersReferenceDict
    )
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    shareable: bool
