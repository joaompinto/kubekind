from attrs import define

from kubekind.kind import SimpleObject


@define
class emptyDir(SimpleObject):
    name: str
    emptyDir: dict = {}
    prefix_key = "volumes"
    include_fields = "emptyDir"
