import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PriorityLevelConfigurationStatus:
    conditions: typing.Optional[
        list[kubernetes_asyncio.client.V1PriorityLevelConfigurationCondition]
    ]

    def __init__(
        self,
        *,
        conditions: typing.Optional[
            list[kubernetes_asyncio.client.V1PriorityLevelConfigurationCondition]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PriorityLevelConfigurationStatusDict: ...

class V1PriorityLevelConfigurationStatusDict(typing.TypedDict, total=False):
    conditions: list[
        kubernetes_asyncio.client.V1PriorityLevelConfigurationConditionDict
    ]
