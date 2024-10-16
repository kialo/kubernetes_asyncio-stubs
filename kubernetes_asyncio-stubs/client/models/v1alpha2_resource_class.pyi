import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha2ResourceClass:
    api_version: str
    driver_name: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    parameters_ref: typing.Optional[
        kubernetes_asyncio.client.V1alpha2ResourceClassParametersReference
    ]
    structured_parameters: typing.Optional[bool]
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
        structured_parameters: typing.Optional[bool] = ...,
        suitable_nodes: typing.Optional[kubernetes_asyncio.client.V1NodeSelector] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2ResourceClassDict: ...

class V1alpha2ResourceClassDict(typing.TypedDict, total=False):
    apiVersion: str
    driverName: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    parametersRef: (
        kubernetes_asyncio.client.V1alpha2ResourceClassParametersReferenceDict
    )
    structuredParameters: bool
    suitableNodes: kubernetes_asyncio.client.V1NodeSelectorDict
