import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1beta3Subject:
    group: typing.Optional[kubernetes_asyncio.client.V1beta3GroupSubject]
    kind: str
    service_account: typing.Optional[
        kubernetes_asyncio.client.V1beta3ServiceAccountSubject
    ]
    user: typing.Optional[kubernetes_asyncio.client.V1beta3UserSubject]

    def __init__(
        self,
        *,
        group: typing.Optional[kubernetes_asyncio.client.V1beta3GroupSubject] = ...,
        kind: str,
        service_account: typing.Optional[
            kubernetes_asyncio.client.V1beta3ServiceAccountSubject
        ] = ...,
        user: typing.Optional[kubernetes_asyncio.client.V1beta3UserSubject] = ...,
    ) -> None: ...
    def to_dict(self) -> V1beta3SubjectDict: ...

class V1beta3SubjectDict(typing.TypedDict, total=False):
    group: typing.Optional[kubernetes_asyncio.client.V1beta3GroupSubjectDict]
    kind: str
    serviceAccount: typing.Optional[
        kubernetes_asyncio.client.V1beta3ServiceAccountSubjectDict
    ]
    user: typing.Optional[kubernetes_asyncio.client.V1beta3UserSubjectDict]
