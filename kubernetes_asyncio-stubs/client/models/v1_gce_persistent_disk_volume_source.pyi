import typing

class V1GCEPersistentDiskVolumeSource:
    fs_type: typing.Optional[str]
    partition: typing.Optional[int]
    pd_name: str
    read_only: typing.Optional[bool]

    def __init__(
        self,
        *,
        fs_type: typing.Optional[str] = ...,
        partition: typing.Optional[int] = ...,
        pd_name: str,
        read_only: typing.Optional[bool] = ...,
    ) -> None: ...
    def to_dict(self) -> V1GCEPersistentDiskVolumeSourceDict: ...

class V1GCEPersistentDiskVolumeSourceDict(typing.TypedDict, total=False):
    fsType: str
    partition: int
    pdName: str
    readOnly: bool
