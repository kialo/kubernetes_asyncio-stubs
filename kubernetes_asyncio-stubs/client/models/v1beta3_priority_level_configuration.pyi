import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta3PriorityLevelConfiguration:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta]
    spec: typing.Optional[
        kubernetes_asyncio.client.V1beta3PriorityLevelConfigurationSpec
    ]
    status: typing.Optional[
        kubernetes_asyncio.client.V1beta3PriorityLevelConfigurationStatus
    ]

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMeta] = ...,
        spec: typing.Optional[
            kubernetes_asyncio.client.V1beta3PriorityLevelConfigurationSpec
        ] = ...,
        status: typing.Optional[
            kubernetes_asyncio.client.V1beta3PriorityLevelConfigurationStatus
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta3PriorityLevelConfigurationDict: ...

class V1beta3PriorityLevelConfigurationDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes_asyncio.client.V1ObjectMetaDict]
    spec: typing.Optional[
        kubernetes_asyncio.client.V1beta3PriorityLevelConfigurationSpecDict
    ]
    status: typing.Optional[
        kubernetes_asyncio.client.V1beta3PriorityLevelConfigurationStatusDict
    ]