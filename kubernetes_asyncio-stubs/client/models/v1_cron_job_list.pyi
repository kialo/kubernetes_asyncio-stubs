import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CronJobList:
    api_version: str
    items: list[kubernetes_asyncio.client.V1CronJob]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1CronJob],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1CronJobListDict: ...

class V1CronJobListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes_asyncio.client.V1CronJobDict]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMetaDict
