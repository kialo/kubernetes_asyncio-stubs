import datetime
import typing

class V1APIServiceCondition:
    last_transition_time: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    status: str
    type: str

    def __init__(
        self,
        *,
        last_transition_time: typing.Optional[datetime.datetime] = ...,
        message: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...,
        status: str,
        type: str,
    ) -> None: ...
    def to_dict(self) -> V1APIServiceConditionDict: ...

class V1APIServiceConditionDict(typing.TypedDict, total=False):
    lastTransitionTime: datetime.datetime
    message: str
    reason: str
    status: str
    type: str
