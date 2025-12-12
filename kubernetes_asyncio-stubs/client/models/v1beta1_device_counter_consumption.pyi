import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1DeviceCounterConsumption:
    counter_set: str
    counters: dict[str, kubernetes_asyncio.client.V1beta1Counter]

    def __init__(
        self,
        *,
        counter_set: str,
        counters: dict[str, kubernetes_asyncio.client.V1beta1Counter],
    ) -> None: ...
    def to_dict(self) -> V1beta1DeviceCounterConsumptionDict: ...

class V1beta1DeviceCounterConsumptionDict(typing.TypedDict, total=False):
    counterSet: str
    counters: dict[str, kubernetes_asyncio.client.V1beta1CounterDict]
