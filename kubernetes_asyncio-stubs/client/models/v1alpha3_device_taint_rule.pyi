import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha3DeviceTaintRule:
    api_version: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMeta
    spec: kubernetes_asyncio.client.V1alpha3DeviceTaintRuleSpec

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: kubernetes_asyncio.client.V1alpha3DeviceTaintRuleSpec,
    ) -> None: ...
    def to_dict(self) -> V1alpha3DeviceTaintRuleDict: ...

class V1alpha3DeviceTaintRuleDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: kubernetes_asyncio.client.V1ObjectMetaDict
    spec: kubernetes_asyncio.client.V1alpha3DeviceTaintRuleSpecDict
