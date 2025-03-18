import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class FlowcontrolV1Subject:
    group: typing.Optional[kubernetes_asyncio.client.V1GroupSubject]
    kind: str
    service_account: typing.Optional[kubernetes_asyncio.client.V1ServiceAccountSubject]
    user: typing.Optional[kubernetes_asyncio.client.V1UserSubject]

    def __init__(
        self,
        *,
        group: typing.Optional[kubernetes_asyncio.client.V1GroupSubject] = ...,
        kind: str,
        service_account: typing.Optional[
            kubernetes_asyncio.client.V1ServiceAccountSubject
        ] = ...,
        user: typing.Optional[kubernetes_asyncio.client.V1UserSubject] = ...,
    ) -> None: ...
    def to_dict(self) -> FlowcontrolV1SubjectDict: ...

class FlowcontrolV1SubjectDict(typing.TypedDict, total=False):
    group: kubernetes_asyncio.client.V1GroupSubjectDict
    kind: str
    serviceAccount: kubernetes_asyncio.client.V1ServiceAccountSubjectDict
    user: kubernetes_asyncio.client.V1UserSubjectDict
