import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta1TypeChecking:
    expression_warnings: typing.Optional[
        list[kubernetes_asyncio.client.V1beta1ExpressionWarning]
    ]

    def __init__(
        self,
        *,
        expression_warnings: typing.Optional[
            list[kubernetes_asyncio.client.V1beta1ExpressionWarning]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta1TypeCheckingDict: ...

class V1beta1TypeCheckingDict(typing.TypedDict, total=False):
    expressionWarnings: typing.Optional[
        list[kubernetes_asyncio.client.V1beta1ExpressionWarningDict]
    ]
