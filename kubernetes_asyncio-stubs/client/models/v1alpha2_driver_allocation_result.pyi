import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha2DriverAllocationResult:
    named_resources: typing.Optional[
        kubernetes_asyncio.client.V1alpha2NamedResourcesAllocationResult
    ]
    vendor_request_parameters: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        named_resources: typing.Optional[
            kubernetes_asyncio.client.V1alpha2NamedResourcesAllocationResult
        ] = ...,
        vendor_request_parameters: typing.Optional[typing.Any] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2DriverAllocationResultDict: ...

class V1alpha2DriverAllocationResultDict(typing.TypedDict, total=False):
    namedResources: kubernetes_asyncio.client.V1alpha2NamedResourcesAllocationResultDict
    vendorRequestParameters: typing.Any
