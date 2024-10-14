import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta3FlowSchemaStatus:
    conditions: typing.Optional[
        list[kubernetes_asyncio.client.V1beta3FlowSchemaCondition]
    ]

    def __init__(
        self,
        *,
        conditions: typing.Optional[
            list[kubernetes_asyncio.client.V1beta3FlowSchemaCondition]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta3FlowSchemaStatusDict: ...

class V1beta3FlowSchemaStatusDict(typing.TypedDict, total=False):
    conditions: list[kubernetes_asyncio.client.V1beta3FlowSchemaConditionDict]
