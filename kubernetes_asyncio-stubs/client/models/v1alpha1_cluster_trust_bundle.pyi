import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1ClusterTrustBundle:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: kubernetes_asyncio.client.V1alpha1ClusterTrustBundleSpec

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: kubernetes_asyncio.client.V1alpha1ClusterTrustBundleSpec,
    ) -> None: ...
    def to_dict(self) -> V1alpha1ClusterTrustBundleDict: ...

class V1alpha1ClusterTrustBundleDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: kubernetes_asyncio.client.V1alpha1ClusterTrustBundleSpecDict
