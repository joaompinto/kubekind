from attrs import define

from kubekind.kind import SimpleObject


@define
class volumeMount(SimpleObject):
    """
    A volume mount

    . [name]: name of the volume to mount
    . [mountPath] : path within the container to use as the mount point
    """

    name: str
    mountPath: str
    prefix_key = "volumeMounts"
