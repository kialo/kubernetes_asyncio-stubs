import typing

class V1AzureDiskVolumeSource:
    caching_mode: typing.Optional[str]
    disk_name: str
    disk_uri: str
    fs_type: typing.Optional[str]
    kind: typing.Optional[str]
    read_only: typing.Optional[bool]

    def __init__(
        self,
        *,
        caching_mode: typing.Optional[str] = ...,
        disk_name: str,
        disk_uri: str,
        fs_type: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        read_only: typing.Optional[bool] = ...,
    ) -> None: ...
    def to_dict(self) -> V1AzureDiskVolumeSourceDict: ...

class V1AzureDiskVolumeSourceDict(typing.TypedDict, total=False):
    cachingMode: str
    diskName: str
    diskURI: str
    fsType: str
    kind: str
    readOnly: bool
