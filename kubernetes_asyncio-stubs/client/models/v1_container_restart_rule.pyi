import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ContainerRestartRule:
    action: str
    exit_codes: typing.Optional[
        kubernetes_asyncio.client.V1ContainerRestartRuleOnExitCodes
    ]

    def __init__(
        self,
        *,
        action: str,
        exit_codes: typing.Optional[
            kubernetes_asyncio.client.V1ContainerRestartRuleOnExitCodes
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ContainerRestartRuleDict: ...

class V1ContainerRestartRuleDict(typing.TypedDict, total=False):
    action: str
    exitCodes: kubernetes_asyncio.client.V1ContainerRestartRuleOnExitCodesDict
