import typing

class V1IngressTLS:
    hosts: typing.Optional[list[str]]
    secret_name: typing.Optional[str]

    def __init__(
        self,
        *,
        hosts: typing.Optional[list[str]] = ...,
        secret_name: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1IngressTLSDict: ...

class V1IngressTLSDict(typing.TypedDict, total=False):
    hosts: list[str]
    secretName: str
