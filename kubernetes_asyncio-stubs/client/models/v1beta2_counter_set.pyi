import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta2CounterSet:
    counters: dict[str, kubernetes_asyncio.client.V1beta2Counter]
    name: str

    def __init__(
        self,
        *,
        counters: dict[str, kubernetes_asyncio.client.V1beta2Counter],
        name: str,
    ) -> None: ...
    def to_dict(self) -> V1beta2CounterSetDict: ...

class V1beta2CounterSetDict(typing.TypedDict, total=False):
    counters: dict[str, kubernetes_asyncio.client.V1beta2CounterDict]
    name: str
