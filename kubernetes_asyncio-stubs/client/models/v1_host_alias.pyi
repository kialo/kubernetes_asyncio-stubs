import typing

class V1HostAlias:
    hostnames: typing.Optional[list[str]]
    ip: typing.Optional[str]

    def __init__(
        self,
        *,
        hostnames: typing.Optional[list[str]] = ...,
        ip: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1HostAliasDict: ...

class V1HostAliasDict(typing.TypedDict, total=False):
    hostnames: list[str]
    ip: str
