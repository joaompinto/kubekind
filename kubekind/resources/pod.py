from attrs import define

from kubekind.kind import Kind

from .container import Container


@define
class Pod(Kind):
    """
    Pod is a collection of containers that can run on a host.
    In a Pod you can define objects of type `Container` and `Volumes`

    Args:
        name: Name of the pod

    Details: https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/"""

    name: str
    apiVersion = "v1"
    allowed_classes = [Container]
