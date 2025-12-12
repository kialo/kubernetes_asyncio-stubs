import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1EndpointHints:
    for_nodes: typing.Optional[list[kubernetes_asyncio.client.V1ForNode]]
    for_zones: typing.Optional[list[kubernetes_asyncio.client.V1ForZone]]

    def __init__(
        self,
        *,
        for_nodes: typing.Optional[list[kubernetes_asyncio.client.V1ForNode]] = ...,
        for_zones: typing.Optional[list[kubernetes_asyncio.client.V1ForZone]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1EndpointHintsDict: ...

class V1EndpointHintsDict(typing.TypedDict, total=False):
    forNodes: list[kubernetes_asyncio.client.V1ForNodeDict]
    forZones: list[kubernetes_asyncio.client.V1ForZoneDict]
