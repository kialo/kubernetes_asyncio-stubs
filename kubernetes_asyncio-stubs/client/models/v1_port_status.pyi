import typing

class V1PortStatus:
    error: typing.Optional[str]
    port: int
    protocol: str

    def __init__(
        self, *, error: typing.Optional[str] = ..., port: int, protocol: str
    ) -> None: ...
    def to_dict(self) -> V1PortStatusDict: ...

class V1PortStatusDict(typing.TypedDict, total=False):
    error: str
    port: int
    protocol: str
