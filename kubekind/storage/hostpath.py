from attrs import define

from kubekind.base import JSONObject


@define
class hostPath(JSONObject):
    """
    hostPath represents a pre-existing file or directory on the host machine
    that is directly exposed to the container. This is generally used for system agents
    or other privileged things that are allowed to see the host machine

    Args:
        path: name of the volume. Must be a DNS_LABEL and unique within the pod.

    Details: https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume/
    """

    path: str
    type: str = ""
