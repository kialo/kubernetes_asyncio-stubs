import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha3DeviceTaintRuleSpec:
    device_selector: typing.Optional[
        kubernetes_asyncio.client.V1alpha3DeviceTaintSelector
    ]
    taint: kubernetes_asyncio.client.V1alpha3DeviceTaint

    def __init__(
        self,
        *,
        device_selector: typing.Optional[
            kubernetes_asyncio.client.V1alpha3DeviceTaintSelector
        ] = ...,
        taint: kubernetes_asyncio.client.V1alpha3DeviceTaint,
    ) -> None: ...
    def to_dict(self) -> V1alpha3DeviceTaintRuleSpecDict: ...

class V1alpha3DeviceTaintRuleSpecDict(typing.TypedDict, total=False):
    deviceSelector: kubernetes_asyncio.client.V1alpha3DeviceTaintSelectorDict
    taint: kubernetes_asyncio.client.V1alpha3DeviceTaintDict
