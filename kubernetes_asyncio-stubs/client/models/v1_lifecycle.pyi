import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1Lifecycle:
    post_start: typing.Optional[kubernetes_asyncio.client.V1LifecycleHandler]
    pre_stop: typing.Optional[kubernetes_asyncio.client.V1LifecycleHandler]
    stop_signal: typing.Optional[str]

    def __init__(
        self,
        *,
        post_start: typing.Optional[kubernetes_asyncio.client.V1LifecycleHandler] = ...,
        pre_stop: typing.Optional[kubernetes_asyncio.client.V1LifecycleHandler] = ...,
        stop_signal: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1LifecycleDict: ...

class V1LifecycleDict(typing.TypedDict, total=False):
    postStart: kubernetes_asyncio.client.V1LifecycleHandlerDict
    preStop: kubernetes_asyncio.client.V1LifecycleHandlerDict
    stopSignal: str
