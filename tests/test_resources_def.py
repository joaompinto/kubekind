import pytest

from kubekind.resources.container import Container
from kubekind.resources.pod import Pod

POD_EXPECTED_RESULT: dict = {
    "kind": "Pod",
    "apiVersion": "v1",
    "metadata": {"name": "my-pod"},
}

CONTAINER_EXPECTED_RESULT: dict = {"name": "bash", "image": "bash:latest"}

POD_CONTAINER_EXPECTED_RESULT = {
    **POD_EXPECTED_RESULT,
    **{"spec": {"containers": [CONTAINER_EXPECTED_RESULT]}},
}


def test_pod_missing_parameter():
    with pytest.raises(TypeError) as _:
        Pod()


def test_pod_def():

    pod = Pod("my-pod")
    assert pod.as_dict() == POD_EXPECTED_RESULT

    container = Container("bash", "bash:latest")
    assert container.as_dict() == CONTAINER_EXPECTED_RESULT

    pod.add(container)
    assert pod.as_dict() == POD_CONTAINER_EXPECTED_RESULT
