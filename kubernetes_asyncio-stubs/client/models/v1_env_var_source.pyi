import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1EnvVarSource:
    config_map_key_ref: typing.Optional[
        kubernetes_asyncio.client.V1ConfigMapKeySelector
    ]
    field_ref: typing.Optional[kubernetes_asyncio.client.V1ObjectFieldSelector]
    file_key_ref: typing.Optional[kubernetes_asyncio.client.V1FileKeySelector]
    resource_field_ref: typing.Optional[
        kubernetes_asyncio.client.V1ResourceFieldSelector
    ]
    secret_key_ref: typing.Optional[kubernetes_asyncio.client.V1SecretKeySelector]

    def __init__(
        self,
        *,
        config_map_key_ref: typing.Optional[
            kubernetes_asyncio.client.V1ConfigMapKeySelector
        ] = ...,
        field_ref: typing.Optional[
            kubernetes_asyncio.client.V1ObjectFieldSelector
        ] = ...,
        file_key_ref: typing.Optional[
            kubernetes_asyncio.client.V1FileKeySelector
        ] = ...,
        resource_field_ref: typing.Optional[
            kubernetes_asyncio.client.V1ResourceFieldSelector
        ] = ...,
        secret_key_ref: typing.Optional[
            kubernetes_asyncio.client.V1SecretKeySelector
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1EnvVarSourceDict: ...

class V1EnvVarSourceDict(typing.TypedDict, total=False):
    configMapKeyRef: kubernetes_asyncio.client.V1ConfigMapKeySelectorDict
    fieldRef: kubernetes_asyncio.client.V1ObjectFieldSelectorDict
    fileKeyRef: kubernetes_asyncio.client.V1FileKeySelectorDict
    resourceFieldRef: kubernetes_asyncio.client.V1ResourceFieldSelectorDict
    secretKeyRef: kubernetes_asyncio.client.V1SecretKeySelectorDict
