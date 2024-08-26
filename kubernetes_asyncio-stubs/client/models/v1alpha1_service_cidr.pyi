import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1ServiceCIDR:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes_asyncio.client.V1alpha1ServiceCIDRSpec]
    status: typing.Optional[kubernetes_asyncio.client.V1alpha1ServiceCIDRStatus]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes_asyncio.client.V1alpha1ServiceCIDRSpec] = ...,
        status: typing.Optional[
            kubernetes_asyncio.client.V1alpha1ServiceCIDRStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1ServiceCIDRDict: ...

class V1alpha1ServiceCIDRDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes_asyncio.client.V1alpha1ServiceCIDRSpecDict]
    status: typing.Optional[kubernetes_asyncio.client.V1alpha1ServiceCIDRStatusDict]
