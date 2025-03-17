import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1Endpoints:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    subsets: typing.Optional[list[kubernetes_asyncio.client.V1EndpointSubset]]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        subsets: typing.Optional[
            list[kubernetes_asyncio.client.V1EndpointSubset]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1EndpointsDict: ...

class V1EndpointsDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    subsets: list[kubernetes_asyncio.client.V1EndpointSubsetDict]
