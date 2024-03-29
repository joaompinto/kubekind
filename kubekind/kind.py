from collections import defaultdict
from typing import Literal

import yaml
from attrs import NOTHING, define, fields
from rich import print as rich_print
from rich import print_json
from rich.syntax import Syntax


class NotAllowedExecption(Exception):
    pass


class Stack:
    """
    Stack singleton to keep track of context managers
    Required the add(None) method
    """

    stack = []

    @classmethod
    def add(cls, item: object):
        return Stack.stack.append(item)

    @classmethod
    def pop(cls):
        return Stack.stack.pop()

    @classmethod
    def tail(cls):
        return Stack.stack[-1]


class RawObject:
    def __attrs_post_init__(self):
        self.obj = {}
        self.childs = []
        self.parent = None
        if Stack.stack:
            self.parent = Stack.tail()

    def print(self, mode: Literal["yaml", "json"] = "yaml"):
        data = self.as_dict()
        if mode == "json":
            print_json(data=data)
        else:
            yaml_output = Syntax(yaml.dump(data, sort_keys=False), "yaml")
            rich_print(yaml_output)

    def __enter__(self):
        Stack.add(self)
        if self.parent:
            self.add()

        return self

    def __exit__(self, type, value, traceback):
        if self.parent:
            Stack.pop()

    def add(self, obj: object = None):
        """
        Add object

        If is None add 'self' to the parent context manager object
        Else add 'obj' as chidl to 'self'
        """
        if obj is None:
            parent = self.parent
            parent.check_is_allowed_class(self)
            parent.childs.append(self)
            self.parent = parent
            return self
        else:
            self.check_is_allowed_class(obj)
            self.childs.append(obj)
            obj.parent = self
            return obj

    def check_is_allowed_class(self, obj: object):
        allowed_classes = getattr(self, "allowed_classes")
        for cls in allowed_classes:
            if isinstance(obj, cls):
                return True
        raise NotAllowedExecption(
            f"'{obj.__class__.__name__}' not allowed in '{self.__class__.__name__}'"
        )

    @property
    def __members__(self):
        member_dict = {}
        for name in dir(self):
            if "__" not in name:
                member_dict[name] = getattr(self, name)
        return member_dict

    def as_dict(self) -> dict:
        members = self.__members__
        expose_dict = {}
        include_fields = getattr(self, "include_fields", [])
        for field in fields(self.__class__):
            value = members[field.name]
            if field.name in include_fields or field.default is NOTHING or value:
                expose_dict[field.name] = value
        extra_dict = defaultdict(list)
        spec_classes = getattr(self, "allowed_classes", [])
        for child in self.childs:
            if child.__class__ in spec_classes:
                extra_dict[child.prefix_key].append(child.as_dict())
        return {**expose_dict, **extra_dict}


class SimpleObject(RawObject):
    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        self.add()


@define
class Kind(RawObject):
    def as_dict(self):
        obj = {
            "kind": self.__class__.__name__,
            "apiVersion": self.apiVersion,
            "metadata": {"name": self.name},
        }
        obj["spec"] = super().as_dict()
        del obj["spec"]["name"]
        return obj
