import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1FlowSchemaStatus:
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1FlowSchemaCondition]]

    def __init__(
        self,
        *,
        conditions: typing.Optional[
            list[kubernetes_asyncio.client.V1FlowSchemaCondition]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1FlowSchemaStatusDict: ...

class V1FlowSchemaStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[
        list[kubernetes_asyncio.client.V1FlowSchemaConditionDict]
    ]
