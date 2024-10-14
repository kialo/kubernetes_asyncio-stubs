import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1APIGroup:
    api_version: str
    kind: str
    name: str
    preferred_version: typing.Optional[
        kubernetes_asyncio.client.V1GroupVersionForDiscovery
    ]
    server_address_by_client_cid_rs: typing.Optional[
        list[kubernetes_asyncio.client.V1ServerAddressByClientCIDR]
    ]
    versions: list[kubernetes_asyncio.client.V1GroupVersionForDiscovery]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        name: str,
        preferred_version: typing.Optional[
            kubernetes_asyncio.client.V1GroupVersionForDiscovery
        ] = ...,
        server_address_by_client_cid_rs: typing.Optional[
            list[kubernetes_asyncio.client.V1ServerAddressByClientCIDR]
        ] = ...,
        versions: list[kubernetes_asyncio.client.V1GroupVersionForDiscovery],
    ) -> None: ...
    def to_dict(self) -> V1APIGroupDict: ...

class V1APIGroupDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    name: str
    preferredVersion: kubernetes_asyncio.client.V1GroupVersionForDiscoveryDict
    serverAddressByClientCIDRs: list[
        kubernetes_asyncio.client.V1ServerAddressByClientCIDRDict
    ]
    versions: list[kubernetes_asyncio.client.V1GroupVersionForDiscoveryDict]
