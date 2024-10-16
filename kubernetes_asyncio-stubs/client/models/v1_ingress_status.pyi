import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1IngressStatus:
    load_balancer: typing.Optional[
        kubernetes_asyncio.client.V1IngressLoadBalancerStatus
    ]

    def __init__(
        self,
        *,
        load_balancer: typing.Optional[
            kubernetes_asyncio.client.V1IngressLoadBalancerStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1IngressStatusDict: ...

class V1IngressStatusDict(typing.TypedDict, total=False):
    loadBalancer: kubernetes_asyncio.client.V1IngressLoadBalancerStatusDict
