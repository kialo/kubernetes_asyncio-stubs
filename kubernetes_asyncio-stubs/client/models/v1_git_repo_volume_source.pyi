import typing

class V1GitRepoVolumeSource:
    directory: typing.Optional[str]
    repository: str
    revision: typing.Optional[str]

    def __init__(
        self,
        *,
        directory: typing.Optional[str] = ...,
        repository: str,
        revision: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1GitRepoVolumeSourceDict: ...

class V1GitRepoVolumeSourceDict(typing.TypedDict, total=False):
    directory: str
    repository: str
    revision: str
