from attrs import define

from kubekind.kind import RawObject


@define
class Container(RawObject):
    """
    A single application container that you want to run within a pod.

    Args:
        name: Name of the container specified as a DNS_LABEL
        image: Container image name
        args: Arguments to the entrypoint. The container image's CMD is used if this is not provided.

    Details: https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#Container
    """

    name: str
    image: str
    args: list[str] = []
    prefix_key = "containers"
