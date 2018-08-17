from collections import defaultdict


def replace_dict_keys(data, new_key_fn):  # type: (dict, (str -> str)) -> dict
    return {new_key_fn(k): data[k] for k in data}


def rename_dict(data, mapping):  # type: (dict, dict) -> dict
    return {v: data[k] for k, v in mapping.items() if v}


def infinite_default_dict():
    return defaultdict(infinite_default_dict)
