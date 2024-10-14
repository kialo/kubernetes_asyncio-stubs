import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1ResourceRequirements:
    claims: typing.Optional[list[kubernetes_asyncio.client.V1ResourceClaim]]
    limits: typing.Optional[dict[str, str]]
    requests: typing.Optional[dict[str, str]]

    def __init__(
        self,
        *,
        claims: typing.Optional[list[kubernetes_asyncio.client.V1ResourceClaim]] = ...,
        limits: typing.Optional[dict[str, str]] = ...,
        requests: typing.Optional[dict[str, str]] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ResourceRequirementsDict: ...

class V1ResourceRequirementsDict(typing.TypedDict, total=False):
    claims: list[kubernetes_asyncio.client.V1ResourceClaimDict]
    limits: dict[str, str]
    requests: dict[str, str]
