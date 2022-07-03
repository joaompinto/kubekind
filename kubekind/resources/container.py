from attrs import define

from kubekind.kind import RawObject
from kubekind.run import run_main


@define
class Container(RawObject):
    """
    A single application container that you want to run within a pod.

    Args:
        name: Name of the container specified as a DNS_LABEL
        image: Container image name

    Details: https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#Container
    """

    name: str
    image: str
    prefix_key = "containers"

    def as_dict(self):
        return {
            "name": self.name,
            "image": self.image,
        }


run_main(Container, __name__)
