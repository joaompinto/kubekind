# kubekind

Library to generate Kubernetes manifests using Python code

[![PyPi](https://img.shields.io/pypi/v/kubekind.svg?style=flat-square)](https://pypi.python.org/pypi/kubekind)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)

# Motivation

Write manifests using Python code to improve readability and getting the benefits of IDEs IntelliSense features.


<div align="center">
  <img valign="middle" src="https://github.com/joaompinto/kubekind/raw/main/imgs/kubekind.png" />
</div>


# Requirements

- Python 3.9+ on Linux, Windows or Mac

# Install
```sh
pip insall kubekind
```
# Generated a pod manifest
```python
# test.py
from kubekind import Pod, Container

with Pod("my-pod") as pod:
    Container("bash", "bash:latest", args=["sleep", "10000"]).add()
    Container("bash_2", "bash:latest", args=["sleep", "10000"]).add()

pod.print()
```
Apply the manifest
```sh
python test.py | kubectl apply -f -
```
