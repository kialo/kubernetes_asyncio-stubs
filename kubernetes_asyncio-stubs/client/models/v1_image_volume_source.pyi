import typing

class V1ImageVolumeSource:
    pull_policy: typing.Optional[str]
    reference: typing.Optional[str]

    def __init__(
        self,
        *,
        pull_policy: typing.Optional[str] = ...,
        reference: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ImageVolumeSourceDict: ...

class V1ImageVolumeSourceDict(typing.TypedDict, total=False):
    pullPolicy: str
    reference: str
