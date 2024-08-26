import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha2ResourceClass:
    api_version: typing.Optional[str]
    driver_name: str
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    parameters_ref: typing.Optional[
        kubernetes_asyncio.client.V1alpha2ResourceClassParametersReference
    ]
    suitable_nodes: typing.Optional[kubernetes_asyncio.client.V1NodeSelector]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        driver_name: str,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        parameters_ref: typing.Optional[
            kubernetes_asyncio.client.V1alpha2ResourceClassParametersReference
        ] = ...,
        suitable_nodes: typing.Optional[kubernetes_asyncio.client.V1NodeSelector] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2ResourceClassDict: ...

class V1alpha2ResourceClassDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    driverName: str
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    parametersRef: typing.Optional[
        kubernetes_asyncio.client.V1alpha2ResourceClassParametersReferenceDict
    ]
    suitableNodes: typing.Optional[kubernetes_asyncio.client.V1NodeSelectorDict]
