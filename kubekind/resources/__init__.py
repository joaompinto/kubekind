"""
This package contains the resource classes corresponding to
https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/ .
"""
from .container import Container
from .pod import Pod

__all__ = ["Container", "Pod"]
