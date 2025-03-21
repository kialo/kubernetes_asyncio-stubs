import typing

class V1alpha1ClusterTrustBundleSpec:
    signer_name: typing.Optional[str]
    trust_bundle: str

    def __init__(
        self, *, signer_name: typing.Optional[str] = ..., trust_bundle: str
    ) -> None: ...
    def to_dict(self) -> V1alpha1ClusterTrustBundleSpecDict: ...

class V1alpha1ClusterTrustBundleSpecDict(typing.TypedDict, total=False):
    signerName: str
    trustBundle: str
