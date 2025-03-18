import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1VolumeProjection:
    cluster_trust_bundle: typing.Optional[
        kubernetes_asyncio.client.V1ClusterTrustBundleProjection
    ]
    config_map: typing.Optional[kubernetes_asyncio.client.V1ConfigMapProjection]
    downward_api: typing.Optional[kubernetes_asyncio.client.V1DownwardAPIProjection]
    secret: typing.Optional[kubernetes_asyncio.client.V1SecretProjection]
    service_account_token: typing.Optional[
        kubernetes_asyncio.client.V1ServiceAccountTokenProjection
    ]

    def __init__(
        self,
        *,
        cluster_trust_bundle: typing.Optional[
            kubernetes_asyncio.client.V1ClusterTrustBundleProjection
        ] = ...,
        config_map: typing.Optional[
            kubernetes_asyncio.client.V1ConfigMapProjection
        ] = ...,
        downward_api: typing.Optional[
            kubernetes_asyncio.client.V1DownwardAPIProjection
        ] = ...,
        secret: typing.Optional[kubernetes_asyncio.client.V1SecretProjection] = ...,
        service_account_token: typing.Optional[
            kubernetes_asyncio.client.V1ServiceAccountTokenProjection
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1VolumeProjectionDict: ...

class V1VolumeProjectionDict(typing.TypedDict, total=False):
    clusterTrustBundle: kubernetes_asyncio.client.V1ClusterTrustBundleProjectionDict
    configMap: kubernetes_asyncio.client.V1ConfigMapProjectionDict
    downwardAPI: kubernetes_asyncio.client.V1DownwardAPIProjectionDict
    secret: kubernetes_asyncio.client.V1SecretProjectionDict
    serviceAccountToken: kubernetes_asyncio.client.V1ServiceAccountTokenProjectionDict
