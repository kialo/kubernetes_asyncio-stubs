import typing

class V1ContainerImage:
    names: typing.Optional[list[str]]
    size_bytes: typing.Optional[int]

    def __init__(
        self,
        *,
        names: typing.Optional[list[str]] = ...,
        size_bytes: typing.Optional[int] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ContainerImageDict: ...

class V1ContainerImageDict(typing.TypedDict, total=False):
    names: list[str]
    sizeBytes: int
