from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def to_yaml(data):
    return dump(data, Dumper=Dumper, default_flow_style=False, allow_unicode=True)


def from_yaml(stream):
    return load(stream, Loader=Loader)


def read_yaml(path):
    with open(path) as f:
        return from_yaml(f.read())


def save_yaml(data, out_path):
    with open(out_path, "w") as f:
        f.write(to_yaml(data))
