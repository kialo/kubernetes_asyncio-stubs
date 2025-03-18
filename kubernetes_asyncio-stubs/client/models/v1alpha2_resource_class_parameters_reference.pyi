import typing

class V1alpha2ResourceClassParametersReference:
    api_group: typing.Optional[str]
    kind: str
    name: str
    namespace: typing.Optional[str]

    def __init__(
        self,
        *,
        api_group: typing.Optional[str] = ...,
        kind: str,
        name: str,
        namespace: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha2ResourceClassParametersReferenceDict: ...

class V1alpha2ResourceClassParametersReferenceDict(typing.TypedDict, total=False):
    apiGroup: str
    kind: str
    name: str
    namespace: str
