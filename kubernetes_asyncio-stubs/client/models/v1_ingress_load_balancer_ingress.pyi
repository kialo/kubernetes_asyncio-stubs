import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1IngressLoadBalancerIngress:
    hostname: typing.Optional[str]
    ip: typing.Optional[str]
    ports: typing.Optional[list[kubernetes_asyncio.client.V1IngressPortStatus]]

    def __init__(
        self,
        *,
        hostname: typing.Optional[str] = ...,
        ip: typing.Optional[str] = ...,
        ports: typing.Optional[
            list[kubernetes_asyncio.client.V1IngressPortStatus]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1IngressLoadBalancerIngressDict: ...

class V1IngressLoadBalancerIngressDict(typing.TypedDict, total=False):
    hostname: str
    ip: str
    ports: list[kubernetes_asyncio.client.V1IngressPortStatusDict]
