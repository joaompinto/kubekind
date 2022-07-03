import pytest
from test_resources_def import (
    CONTAINER_EXPECTED_RESULT,
    POD_CONTAINER_EXPECTED_RESULT,
    POD_EXPECTED_RESULT,
)

from kubekind.resources.container import Container
from kubekind.resources.pod import Pod


def test_pod_missing_parameter():
    with pytest.raises(TypeError) as _:
        with Pod():
            pass


def test_pod_def():

    with Pod("my-pod") as pod:
        assert pod.as_dict() == POD_EXPECTED_RESULT
        container = Container("bash", "bash:latest").add()
        assert container.as_dict() == CONTAINER_EXPECTED_RESULT
    assert pod.as_dict() == POD_CONTAINER_EXPECTED_RESULT
    pod.print("json")
    pod.print("yaml")
