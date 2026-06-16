import datetime
import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1alpha1PodCertificateRequestStatus:
    begin_refresh_at: typing.Optional[datetime.datetime]
    certificate_chain: typing.Optional[str]
    conditions: typing.Optional[list[kubernetes_asyncio.client.V1Condition]]
    not_after: typing.Optional[datetime.datetime]
    not_before: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        begin_refresh_at: typing.Optional[datetime.datetime] = ...,
        certificate_chain: typing.Optional[str] = ...,
        conditions: typing.Optional[list[kubernetes_asyncio.client.V1Condition]] = ...,
        not_after: typing.Optional[datetime.datetime] = ...,
        not_before: typing.Optional[datetime.datetime] = ...,
    ) -> None: ...
    def to_dict(self) -> V1alpha1PodCertificateRequestStatusDict: ...

class V1alpha1PodCertificateRequestStatusDict(typing.TypedDict, total=False):
    beginRefreshAt: datetime.datetime
    certificateChain: str
    conditions: list[kubernetes_asyncio.client.V1ConditionDict]
    notAfter: datetime.datetime
    notBefore: datetime.datetime
