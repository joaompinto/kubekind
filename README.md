# kubekind

Python library to generate Kubernetes manifests


[![PyPi](https://img.shields.io/pypi/v/kubekind.svg?style=flat-square)](https://pypi.python.org/pypi/kubekind)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)

# Install
```sh
pip insall kubekind
 kubekind
```
# Using
```python
from kubekind import Pod, Container

with Pod("my-pod") as pod:
    Container("bash", "bash:latest").add()

pod.print()
```
