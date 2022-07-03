from collections import defaultdict

from attrs import define
from rich import print_json


class NotAllowedExecption(Exception):
    pass


class Stack:
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
    def __init__(self):
        self.obj = {}
        self.childs = []

    def print(self):
        print_json(data=self.as_dict())

    def __enter__(self):
        if Stack.stack:
            parent = self.add()
        else:
            Stack.add(self)
            parent = None
        self.parent = parent
        return self

    def __exit__(self, type, value, traceback):
        Stack.pop()

    def add(self):
        """add this object to the current context"""
        Stack.tail().childs.append(self)
        return self


@define
class Kind(RawObject):
    def __attrs_pre_init__(self):
        super().__init__()

    def as_dict(self):
        obj = {
            "kind": self.__class__.__name__,
            "apiVersion": self.apiVersion,
            "metadata": {"name": self.name},
        }
        spec_classes = getattr(self, "allowed_classes", [])
        extra_dict = defaultdict(list)
        for child in self.childs:
            if child.__class__ in spec_classes:
                extra_dict[child.prefix_key].append(child.as_dict())
        spec_dict = {}
        if extra_dict:
            spec_dict = {"spec": dict(extra_dict)}
        return dict(obj, **spec_dict)

    def check_is_allowed_spec(self, obj: object):
        allowed_classes = getattr(self, "allowed_classes")
        for cls in allowed_classes:
            if isinstance(obj, cls):
                return True
        raise NotAllowedExecption(
            f"'{obj.__class__.__name__}' not allowed in '{self.__class__.__name__}'"
        )

    def add(self, obj: object):
        """add an object to the current object specs"""
        self.check_is_allowed_spec(obj)
        self.childs.append(obj)
