from collections import defaultdict
from .dict_helper import infinite_default_dict


def group_by(data_list, get_group_key):
    groups = defaultdict(list)
    for x in data_list:
        key = get_group_key(x)
        groups[key].append(x)
    return groups


def group_by_function_list(data_list, get_key_fn_list):
    if len(get_key_fn_list) == 1:
        return group_by(data_list, get_key_fn_list[0])
    else:
        groups = group_by(data_list, get_key_fn_list[0])
        return {
            k: group_by_function_list(v, get_key_fn_list[1:])
            for k, v in groups.itmes()
        }
