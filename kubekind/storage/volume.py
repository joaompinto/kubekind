from attrs import define

from kubekind.base import Kind


@define
class Volume(Kind):
    """
    Volume represents a named volume in a pod that may be accessed by any container in the pod.

    Args:
        name: name of the volume. Must be a DNS_LABEL and unique within the pod.

    Details: https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/volume/
    """

    name: str
    apiVersion = "v1"
