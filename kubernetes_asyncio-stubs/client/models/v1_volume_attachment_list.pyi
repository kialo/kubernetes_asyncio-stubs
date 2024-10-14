import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1VolumeAttachmentList:
    api_version: str
    items: list[kubernetes_asyncio.client.V1VolumeAttachment]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMeta

    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes_asyncio.client.V1VolumeAttachment],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes_asyncio.client.V1ListMeta] = ...,
    ) -> None: ...
    def to_dict(self) -> V1VolumeAttachmentListDict: ...

class V1VolumeAttachmentListDict(typing.TypedDict, total=False):
    apiVersion: str
    items: list[kubernetes_asyncio.client.V1VolumeAttachmentDict]
    kind: str
    metadata: kubernetes_asyncio.client.V1ListMetaDict
