import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1CounterSet:
    counters: dict[str, kubernetes_asyncio.client.V1Counter]
    name: str

    def __init__(
        self, *, counters: dict[str, kubernetes_asyncio.client.V1Counter], name: str
    ) -> None: ...
    def to_dict(self) -> V1CounterSetDict: ...

class V1CounterSetDict(typing.TypedDict, total=False):
    counters: dict[str, kubernetes_asyncio.client.V1CounterDict]
    name: str
