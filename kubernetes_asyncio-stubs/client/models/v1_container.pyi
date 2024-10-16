import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1Container:
    args: typing.Optional[list[str]]
    command: typing.Optional[list[str]]
    env: typing.Optional[list[kubernetes_asyncio.client.V1EnvVar]]
    env_from: typing.Optional[list[kubernetes_asyncio.client.V1EnvFromSource]]
    image: typing.Optional[str]
    image_pull_policy: typing.Optional[str]
    lifecycle: typing.Optional[kubernetes_asyncio.client.V1Lifecycle]
    liveness_probe: typing.Optional[kubernetes_asyncio.client.V1Probe]
    name: str
    ports: typing.Optional[list[kubernetes_asyncio.client.V1ContainerPort]]
    readiness_probe: typing.Optional[kubernetes_asyncio.client.V1Probe]
    resize_policy: typing.Optional[
        list[kubernetes_asyncio.client.V1ContainerResizePolicy]
    ]
    resources: typing.Optional[kubernetes_asyncio.client.V1ResourceRequirements]
    restart_policy: typing.Optional[str]
    security_context: typing.Optional[kubernetes_asyncio.client.V1SecurityContext]
    startup_probe: typing.Optional[kubernetes_asyncio.client.V1Probe]
    stdin: typing.Optional[bool]
    stdin_once: typing.Optional[bool]
    termination_message_path: typing.Optional[str]
    termination_message_policy: typing.Optional[str]
    tty: typing.Optional[bool]
    volume_devices: typing.Optional[list[kubernetes_asyncio.client.V1VolumeDevice]]
    volume_mounts: typing.Optional[list[kubernetes_asyncio.client.V1VolumeMount]]
    working_dir: typing.Optional[str]

    def __init__(
        self,
        *,
        args: typing.Optional[list[str]] = ...,
        command: typing.Optional[list[str]] = ...,
        env: typing.Optional[list[kubernetes_asyncio.client.V1EnvVar]] = ...,
        env_from: typing.Optional[
            list[kubernetes_asyncio.client.V1EnvFromSource]
        ] = ...,
        image: typing.Optional[str] = ...,
        image_pull_policy: typing.Optional[str] = ...,
        lifecycle: typing.Optional[kubernetes_asyncio.client.V1Lifecycle] = ...,
        liveness_probe: typing.Optional[kubernetes_asyncio.client.V1Probe] = ...,
        name: str,
        ports: typing.Optional[list[kubernetes_asyncio.client.V1ContainerPort]] = ...,
        readiness_probe: typing.Optional[kubernetes_asyncio.client.V1Probe] = ...,
        resize_policy: typing.Optional[
            list[kubernetes_asyncio.client.V1ContainerResizePolicy]
        ] = ...,
        resources: typing.Optional[
            kubernetes_asyncio.client.V1ResourceRequirements
        ] = ...,
        restart_policy: typing.Optional[str] = ...,
        security_context: typing.Optional[
            kubernetes_asyncio.client.V1SecurityContext
        ] = ...,
        startup_probe: typing.Optional[kubernetes_asyncio.client.V1Probe] = ...,
        stdin: typing.Optional[bool] = ...,
        stdin_once: typing.Optional[bool] = ...,
        termination_message_path: typing.Optional[str] = ...,
        termination_message_policy: typing.Optional[str] = ...,
        tty: typing.Optional[bool] = ...,
        volume_devices: typing.Optional[
            list[kubernetes_asyncio.client.V1VolumeDevice]
        ] = ...,
        volume_mounts: typing.Optional[
            list[kubernetes_asyncio.client.V1VolumeMount]
        ] = ...,
        working_dir: typing.Optional[str] = ...,
    ) -> None: ...
    def to_dict(self) -> V1ContainerDict: ...

class V1ContainerDict(typing.TypedDict, total=False):
    args: list[str]
    command: list[str]
    env: list[kubernetes_asyncio.client.V1EnvVarDict]
    envFrom: list[kubernetes_asyncio.client.V1EnvFromSourceDict]
    image: str
    imagePullPolicy: str
    lifecycle: kubernetes_asyncio.client.V1LifecycleDict
    livenessProbe: kubernetes_asyncio.client.V1ProbeDict
    name: str
    ports: list[kubernetes_asyncio.client.V1ContainerPortDict]
    readinessProbe: kubernetes_asyncio.client.V1ProbeDict
    resizePolicy: list[kubernetes_asyncio.client.V1ContainerResizePolicyDict]
    resources: kubernetes_asyncio.client.V1ResourceRequirementsDict
    restartPolicy: str
    securityContext: kubernetes_asyncio.client.V1SecurityContextDict
    startupProbe: kubernetes_asyncio.client.V1ProbeDict
    stdin: bool
    stdinOnce: bool
    terminationMessagePath: str
    terminationMessagePolicy: str
    tty: bool
    volumeDevices: list[kubernetes_asyncio.client.V1VolumeDeviceDict]
    volumeMounts: list[kubernetes_asyncio.client.V1VolumeMountDict]
    workingDir: str
