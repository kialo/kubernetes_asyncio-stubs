import typing

class V2MetricTarget:
    average_utilization: typing.Optional[int]
    average_value: typing.Optional[str]
    type: str
    value: typing.Optional[str]

    def __init__(
        self,
        *,
        average_utilization: typing.Optional[int] = ...,
        average_value: typing.Optional[str] = ...,
        type: str,
        value: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V2MetricTargetDict: ...

class V2MetricTargetDict(typing.TypedDict, total=False):
    averageUtilization: int
    averageValue: str
    type: str
    value: str
