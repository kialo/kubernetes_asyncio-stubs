import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1LimitedPriorityLevelConfiguration:
    borrowing_limit_percent: typing.Optional[int]
    lendable_percent: typing.Optional[int]
    limit_response: typing.Optional[kubernetes_asyncio.client.V1LimitResponse]
    nominal_concurrency_shares: typing.Optional[int]

    def __init__(
        self,
        *,
        borrowing_limit_percent: typing.Optional[int] = ...,
        lendable_percent: typing.Optional[int] = ...,
        limit_response: typing.Optional[
            kubernetes_asyncio.client.V1LimitResponse
        ] = ...,
        nominal_concurrency_shares: typing.Optional[int] = ...,
    ) -> None: ...
    def to_dict(self) -> V1LimitedPriorityLevelConfigurationDict: ...

class V1LimitedPriorityLevelConfigurationDict(typing.TypedDict, total=False):
    borrowingLimitPercent: typing.Optional[int]
    lendablePercent: typing.Optional[int]
    limitResponse: typing.Optional[kubernetes_asyncio.client.V1LimitResponseDict]
    nominalConcurrencyShares: typing.Optional[int]
