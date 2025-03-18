import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1ParamRef:
    name: typing.Optional[str]
    namespace: typing.Optional[str]
    parameter_not_found_action: typing.Optional[str]
    selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector]

    def __init__(
        self,
        *,
        name: typing.Optional[str] = ...,
        namespace: typing.Optional[str] = ...,
        parameter_not_found_action: typing.Optional[str] = ...,
        selector: typing.Optional[kubernetes_asyncio.client.V1LabelSelector] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1ParamRefDict: ...

class V1alpha1ParamRefDict(typing.TypedDict, total=False):
    name: str
    namespace: str
    parameterNotFoundAction: str
    selector: kubernetes_asyncio.client.V1LabelSelectorDict
