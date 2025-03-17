import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1SecurityContext:
    allow_privilege_escalation: typing.Optional[bool]
    app_armor_profile: typing.Optional[kubernetes_asyncio.client.V1AppArmorProfile]
    capabilities: typing.Optional[kubernetes_asyncio.client.V1Capabilities]
    privileged: typing.Optional[bool]
    proc_mount: typing.Optional[str]
    read_only_root_filesystem: typing.Optional[bool]
    run_as_group: typing.Optional[int]
    run_as_non_root: typing.Optional[bool]
    run_as_user: typing.Optional[int]
    se_linux_options: typing.Optional[kubernetes_asyncio.client.V1SELinuxOptions]
    seccomp_profile: typing.Optional[kubernetes_asyncio.client.V1SeccompProfile]
    windows_options: typing.Optional[
        kubernetes_asyncio.client.V1WindowsSecurityContextOptions
    ]

    def __init__(
        self,
        *,
        allow_privilege_escalation: typing.Optional[bool] = ...,
        app_armor_profile: typing.Optional[
            kubernetes_asyncio.client.V1AppArmorProfile
        ] = ...,
        capabilities: typing.Optional[kubernetes_asyncio.client.V1Capabilities] = ...,
        privileged: typing.Optional[bool] = ...,
        proc_mount: typing.Optional[str] = ...,
        read_only_root_filesystem: typing.Optional[bool] = ...,
        run_as_group: typing.Optional[int] = ...,
        run_as_non_root: typing.Optional[bool] = ...,
        run_as_user: typing.Optional[int] = ...,
        se_linux_options: typing.Optional[
            kubernetes_asyncio.client.V1SELinuxOptions
        ] = ...,
        seccomp_profile: typing.Optional[
            kubernetes_asyncio.client.V1SeccompProfile
        ] = ...,
        windows_options: typing.Optional[
            kubernetes_asyncio.client.V1WindowsSecurityContextOptions
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1SecurityContextDict: ...

class V1SecurityContextDict(typing.TypedDict, total=False):
    allowPrivilegeEscalation: bool
    appArmorProfile: kubernetes_asyncio.client.V1AppArmorProfileDict
    capabilities: kubernetes_asyncio.client.V1CapabilitiesDict
    privileged: bool
    procMount: str
    readOnlyRootFilesystem: bool
    runAsGroup: int
    runAsNonRoot: bool
    runAsUser: int
    seLinuxOptions: kubernetes_asyncio.client.V1SELinuxOptionsDict
    seccompProfile: kubernetes_asyncio.client.V1SeccompProfileDict
    windowsOptions: kubernetes_asyncio.client.V1WindowsSecurityContextOptionsDict
