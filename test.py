from kubekind import Container, Pod
from kubekind.storage.emptydir import emptyDir
from kubekind.storage.volumemount import volumeMount

with Pod("my-pod") as pod:
    emptyDir("shared-data")  # Shared empty dir between containers

    with Container("bash", "bash:latest", args=["sleep", "10000"]):
        volumeMount("shared-data", "/cache1")

    with Container("bash2", "bash:latest", args=["sleep", "10000"]):
        volumeMount("shared-data", "/cache2")

pod.print()
