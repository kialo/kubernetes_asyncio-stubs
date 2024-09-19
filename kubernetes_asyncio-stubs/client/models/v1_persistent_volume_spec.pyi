import kubernetes_asyncio.client
import kubernetes_asyncio.client.api_client
import typing

class V1PersistentVolumeSpec:
    access_modes: typing.Optional[list[str]]
    aws_elastic_block_store: typing.Optional[
        kubernetes_asyncio.client.V1AWSElasticBlockStoreVolumeSource
    ]
    azure_disk: typing.Optional[kubernetes_asyncio.client.V1AzureDiskVolumeSource]
    azure_file: typing.Optional[
        kubernetes_asyncio.client.V1AzureFilePersistentVolumeSource
    ]
    capacity: typing.Optional[dict[str, str]]
    cephfs: typing.Optional[kubernetes_asyncio.client.V1CephFSPersistentVolumeSource]
    cinder: typing.Optional[kubernetes_asyncio.client.V1CinderPersistentVolumeSource]
    claim_ref: typing.Optional[kubernetes_asyncio.client.V1ObjectReference]
    csi: typing.Optional[kubernetes_asyncio.client.V1CSIPersistentVolumeSource]
    fc: typing.Optional[kubernetes_asyncio.client.V1FCVolumeSource]
    flex_volume: typing.Optional[kubernetes_asyncio.client.V1FlexPersistentVolumeSource]
    flocker: typing.Optional[kubernetes_asyncio.client.V1FlockerVolumeSource]
    gce_persistent_disk: typing.Optional[
        kubernetes_asyncio.client.V1GCEPersistentDiskVolumeSource
    ]
    glusterfs: typing.Optional[
        kubernetes_asyncio.client.V1GlusterfsPersistentVolumeSource
    ]
    host_path: typing.Optional[kubernetes_asyncio.client.V1HostPathVolumeSource]
    iscsi: typing.Optional[kubernetes_asyncio.client.V1ISCSIPersistentVolumeSource]
    local: typing.Optional[kubernetes_asyncio.client.V1LocalVolumeSource]
    mount_options: typing.Optional[list[str]]
    nfs: typing.Optional[kubernetes_asyncio.client.V1NFSVolumeSource]
    node_affinity: typing.Optional[kubernetes_asyncio.client.V1VolumeNodeAffinity]
    persistent_volume_reclaim_policy: typing.Optional[str]
    photon_persistent_disk: typing.Optional[
        kubernetes_asyncio.client.V1PhotonPersistentDiskVolumeSource
    ]
    portworx_volume: typing.Optional[kubernetes_asyncio.client.V1PortworxVolumeSource]
    quobyte: typing.Optional[kubernetes_asyncio.client.V1QuobyteVolumeSource]
    rbd: typing.Optional[kubernetes_asyncio.client.V1RBDPersistentVolumeSource]
    scale_io: typing.Optional[kubernetes_asyncio.client.V1ScaleIOPersistentVolumeSource]
    storage_class_name: typing.Optional[str]
    storageos: typing.Optional[
        kubernetes_asyncio.client.V1StorageOSPersistentVolumeSource
    ]
    volume_attributes_class_name: typing.Optional[str]
    volume_mode: typing.Optional[str]
    vsphere_volume: typing.Optional[
        kubernetes_asyncio.client.V1VsphereVirtualDiskVolumeSource
    ]

    def __init__(
        self,
        *,
        access_modes: typing.Optional[list[str]] = ...,
        aws_elastic_block_store: typing.Optional[
            kubernetes_asyncio.client.V1AWSElasticBlockStoreVolumeSource
        ] = ...,
        azure_disk: typing.Optional[
            kubernetes_asyncio.client.V1AzureDiskVolumeSource
        ] = ...,
        azure_file: typing.Optional[
            kubernetes_asyncio.client.V1AzureFilePersistentVolumeSource
        ] = ...,
        capacity: typing.Optional[dict[str, str]] = ...,
        cephfs: typing.Optional[
            kubernetes_asyncio.client.V1CephFSPersistentVolumeSource
        ] = ...,
        cinder: typing.Optional[
            kubernetes_asyncio.client.V1CinderPersistentVolumeSource
        ] = ...,
        claim_ref: typing.Optional[kubernetes_asyncio.client.V1ObjectReference] = ...,
        csi: typing.Optional[
            kubernetes_asyncio.client.V1CSIPersistentVolumeSource
        ] = ...,
        fc: typing.Optional[kubernetes_asyncio.client.V1FCVolumeSource] = ...,
        flex_volume: typing.Optional[
            kubernetes_asyncio.client.V1FlexPersistentVolumeSource
        ] = ...,
        flocker: typing.Optional[kubernetes_asyncio.client.V1FlockerVolumeSource] = ...,
        gce_persistent_disk: typing.Optional[
            kubernetes_asyncio.client.V1GCEPersistentDiskVolumeSource
        ] = ...,
        glusterfs: typing.Optional[
            kubernetes_asyncio.client.V1GlusterfsPersistentVolumeSource
        ] = ...,
        host_path: typing.Optional[
            kubernetes_asyncio.client.V1HostPathVolumeSource
        ] = ...,
        iscsi: typing.Optional[
            kubernetes_asyncio.client.V1ISCSIPersistentVolumeSource
        ] = ...,
        local: typing.Optional[kubernetes_asyncio.client.V1LocalVolumeSource] = ...,
        mount_options: typing.Optional[list[str]] = ...,
        nfs: typing.Optional[kubernetes_asyncio.client.V1NFSVolumeSource] = ...,
        node_affinity: typing.Optional[
            kubernetes_asyncio.client.V1VolumeNodeAffinity
        ] = ...,
        persistent_volume_reclaim_policy: typing.Optional[str] = ...,
        photon_persistent_disk: typing.Optional[
            kubernetes_asyncio.client.V1PhotonPersistentDiskVolumeSource
        ] = ...,
        portworx_volume: typing.Optional[
            kubernetes_asyncio.client.V1PortworxVolumeSource
        ] = ...,
        quobyte: typing.Optional[kubernetes_asyncio.client.V1QuobyteVolumeSource] = ...,
        rbd: typing.Optional[
            kubernetes_asyncio.client.V1RBDPersistentVolumeSource
        ] = ...,
        scale_io: typing.Optional[
            kubernetes_asyncio.client.V1ScaleIOPersistentVolumeSource
        ] = ...,
        storage_class_name: typing.Optional[str] = ...,
        storageos: typing.Optional[
            kubernetes_asyncio.client.V1StorageOSPersistentVolumeSource
        ] = ...,
        volume_attributes_class_name: typing.Optional[str] = ...,
        volume_mode: typing.Optional[str] = ...,
        vsphere_volume: typing.Optional[
            kubernetes_asyncio.client.V1VsphereVirtualDiskVolumeSource
        ] = ...,
    ) -> None: ...
    def to_dict(self) -> V1PersistentVolumeSpecDict: ...

class V1PersistentVolumeSpecDict(typing.TypedDict, total=False):
    accessModes: typing.Optional[list[str]]
    awsElasticBlockStore: typing.Optional[
        kubernetes_asyncio.client.V1AWSElasticBlockStoreVolumeSourceDict
    ]
    azureDisk: typing.Optional[kubernetes_asyncio.client.V1AzureDiskVolumeSourceDict]
    azureFile: typing.Optional[
        kubernetes_asyncio.client.V1AzureFilePersistentVolumeSourceDict
    ]
    capacity: typing.Optional[dict[str, str]]
    cephfs: typing.Optional[
        kubernetes_asyncio.client.V1CephFSPersistentVolumeSourceDict
    ]
    cinder: typing.Optional[
        kubernetes_asyncio.client.V1CinderPersistentVolumeSourceDict
    ]
    claimRef: typing.Optional[kubernetes_asyncio.client.V1ObjectReferenceDict]
    csi: typing.Optional[kubernetes_asyncio.client.V1CSIPersistentVolumeSourceDict]
    fc: typing.Optional[kubernetes_asyncio.client.V1FCVolumeSourceDict]
    flexVolume: typing.Optional[
        kubernetes_asyncio.client.V1FlexPersistentVolumeSourceDict
    ]
    flocker: typing.Optional[kubernetes_asyncio.client.V1FlockerVolumeSourceDict]
    gcePersistentDisk: typing.Optional[
        kubernetes_asyncio.client.V1GCEPersistentDiskVolumeSourceDict
    ]
    glusterfs: typing.Optional[
        kubernetes_asyncio.client.V1GlusterfsPersistentVolumeSourceDict
    ]
    hostPath: typing.Optional[kubernetes_asyncio.client.V1HostPathVolumeSourceDict]
    iscsi: typing.Optional[kubernetes_asyncio.client.V1ISCSIPersistentVolumeSourceDict]
    local: typing.Optional[kubernetes_asyncio.client.V1LocalVolumeSourceDict]
    mountOptions: typing.Optional[list[str]]
    nfs: typing.Optional[kubernetes_asyncio.client.V1NFSVolumeSourceDict]
    nodeAffinity: typing.Optional[kubernetes_asyncio.client.V1VolumeNodeAffinityDict]
    persistentVolumeReclaimPolicy: typing.Optional[str]
    photonPersistentDisk: typing.Optional[
        kubernetes_asyncio.client.V1PhotonPersistentDiskVolumeSourceDict
    ]
    portworxVolume: typing.Optional[
        kubernetes_asyncio.client.V1PortworxVolumeSourceDict
    ]
    quobyte: typing.Optional[kubernetes_asyncio.client.V1QuobyteVolumeSourceDict]
    rbd: typing.Optional[kubernetes_asyncio.client.V1RBDPersistentVolumeSourceDict]
    scaleIO: typing.Optional[
        kubernetes_asyncio.client.V1ScaleIOPersistentVolumeSourceDict
    ]
    storageClassName: typing.Optional[str]
    storageos: typing.Optional[
        kubernetes_asyncio.client.V1StorageOSPersistentVolumeSourceDict
    ]
    volumeAttributesClassName: typing.Optional[str]
    volumeMode: typing.Optional[str]
    vsphereVolume: typing.Optional[
        kubernetes_asyncio.client.V1VsphereVirtualDiskVolumeSourceDict
    ]
