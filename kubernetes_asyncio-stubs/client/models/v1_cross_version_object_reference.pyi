import typing

class V1CrossVersionObjectReference:
    api_version: str
    kind: str
    name: str

    def __init__(
        self, *, api_version: typing.Optional[str] = ..., kind: str, name: str
    ) -> None: ...
    def to_dict(self) -> V1CrossVersionObjectReferenceDict: ...

class V1CrossVersionObjectReferenceDict(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    name: str
