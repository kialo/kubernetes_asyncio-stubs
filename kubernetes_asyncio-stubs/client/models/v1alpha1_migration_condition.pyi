import datetime
import typing

class V1alpha1MigrationCondition:
    last_update_time: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    status: str
    type: str

    def __init__(
        self,
        *,
        last_update_time: typing.Optional[datetime.datetime] = ...,
        message: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...,
        status: str,
        type: str,
    ) -> None: ...
    def to_dict(self) -> V1alpha1MigrationConditionDict: ...

class V1alpha1MigrationConditionDict(typing.TypedDict, total=False):
    lastUpdateTime: datetime.datetime
    message: str
    reason: str
    status: str
    type: str