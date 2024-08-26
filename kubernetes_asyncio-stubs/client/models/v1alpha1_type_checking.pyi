import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1TypeChecking:
    expression_warnings: typing.Optional[
        list[kubernetes_asyncio.client.V1alpha1ExpressionWarning]
    ]

    def __init__(
        self,
        *,
        expression_warnings: typing.Optional[
            list[kubernetes_asyncio.client.V1alpha1ExpressionWarning]
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1TypeCheckingDict: ...

class V1alpha1TypeCheckingDict(typing.TypedDict, total=False):
    expressionWarnings: typing.Optional[
        list[kubernetes_asyncio.client.V1alpha1ExpressionWarningDict]
    ]
