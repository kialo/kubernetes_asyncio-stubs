import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1PodCertificateRequest:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1alpha1PodCertificateRequestSpec
    status: kubernetes_asyncio.client.V1alpha1PodCertificateRequestStatus

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: kubernetes_asyncio.client.V1alpha1PodCertificateRequestSpec,
        status: typing.Optional[
            kubernetes_asyncio.client.V1alpha1PodCertificateRequestStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1PodCertificateRequestDict: ...

class V1alpha1PodCertificateRequestDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1alpha1PodCertificateRequestSpecDict
    status: kubernetes_asyncio.client.V1alpha1PodCertificateRequestStatusDict
