from attrs import define

from kubekind.kind import Kind
from kubekind.run import run_main

from .container import Container


@define
class Pod(Kind):
    """
    Pod is a collection of containers that can run on a host.

    Details: https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/"""

    name: str
    apiVersion = "v1"
    allowed_classes = [Container]


run_main(Pod, __name__)
