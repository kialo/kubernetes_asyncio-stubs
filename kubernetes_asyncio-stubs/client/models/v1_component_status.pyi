import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ComponentStatus:
    api_version: str
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1ComponentCondition]]
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        conditions: typing.Optional[
            list[kubernetes_asyncio.client.V1ComponentCondition]
        ] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ComponentStatusDict: ...

class V1ComponentStatusDict(typing.TypedDict, total=False):
    apiVersion: str
    conditions: list[kubernetes_asyncio.client.V1ComponentConditionDict]
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
