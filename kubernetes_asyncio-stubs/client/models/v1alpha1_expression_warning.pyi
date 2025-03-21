import typing

class V1alpha1ExpressionWarning:
    field_ref: str
    warning: str

    def __init__(self, *, field_ref: str, warning: str) -> None: ...
    def to_dict(self) -> V1alpha1ExpressionWarningDict: ...

class V1alpha1ExpressionWarningDict(typing.TypedDict, total=False):
    fieldRef: str
    warning: str
