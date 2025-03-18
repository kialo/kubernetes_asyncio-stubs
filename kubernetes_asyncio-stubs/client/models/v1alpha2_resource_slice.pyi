import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha2ResourceSlice:
    api_version: str
    driver_name: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    named_resources: typing.Optional[
        kubernetes_asyncio.client.V1alpha2NamedResourcesResources
    ]
    node_name: typing.Optional[str]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        driver_name: str,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        named_resources: typing.Optional[
            kubernetes_asyncio.client.V1alpha2NamedResourcesResources
        ] = ...,
        node_name: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2ResourceSliceDict: ...

class V1alpha2ResourceSliceDict(typing.TypedDict, total=False):
    apiVersion: str
    driverName: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    namedResources: kubernetes_asyncio.client.V1alpha2NamedResourcesResourcesDict
    nodeName: str
