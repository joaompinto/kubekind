from kubekind import Container, Pod

with Pod("my-pod") as pod:
    Container("bash", "bash:latest", args=["sleep", "10000"]).add()
    Container("bash_2", "bash:latest", args=["sleep", "10000"]).add()

pod.print()
