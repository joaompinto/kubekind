import sys


def run_main(cls: type, name):
    if name == "__main__":
        obj = cls(*sys.argv[1:])
        obj.print()
