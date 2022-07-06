from typing import Union

from attrs import define

from kubekind.base import Giga, JSONObject, Kilo, Kind, Mega


@define
class PVSpec(JSONObject):
    """

    Args:
        JSONObject ([type]): [description]
    """

    accessModes: list[str]
    capacity: Union[Giga, Mega, Kilo]
    mountOptions: list[str] = []
    storageClassName = None


@define
class PersistentVolume(Kind):
    """
    PersistentVolume (PV) is a storage resource provisioned by an administrator.

    Args:
        name: name of the volume. Must be a DNS_LABEL and unique within the pod.

    Details: https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-v1/
    """

    name: str
    apiVersion = "v1"
    spec: PVSpec
