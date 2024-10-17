import typing

class V1ResourceAttributes:
    group: typing.Optional[str]
    name: typing.Optional[str]
    namespace: typing.Optional[str]
    resource: typing.Optional[str]
    subresource: typing.Optional[str]
    verb: typing.Optional[str]
    version: typing.Optional[str]

    def __init__(
        self,
        *,
        group: typing.Optional[str] = ...,
        name: typing.Optional[str] = ...,
        namespace: typing.Optional[str] = ...,
        resource: typing.Optional[str] = ...,
        subresource: typing.Optional[str] = ...,
        verb: typing.Optional[str] = ...,
        version: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ResourceAttributesDict: ...

class V1ResourceAttributesDict(typing.TypedDict, total=False):
    group: str
    name: str
    namespace: str
    resource: str
    subresource: str
    verb: str
    version: str