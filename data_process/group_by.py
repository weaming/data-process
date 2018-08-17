from collections import defaultdict
from .dict_helper import infinite_default_dict


def group_by(data_list, get_group_key, item_fn=None, tail_list_fn=None):
    groups = defaultdict(list)
    for x in data_list:
        key = get_group_key(x)
        if isinstance(key, (list, tuple)):
            for k in key:
                groups[k].append(item_fn(x) if item_fn else x)
        else:
            groups[key].append(item_fn(x) if item_fn else x)

    if tail_list_fn:
        return {k: tail_list_fn(v) for k, v in groups.items()}

    return dict(groups)


def group_by_function_list(
    data_list, get_key_fn_list, item_fn=None, tail_list_fn=None
):
    if len(get_key_fn_list) == 1:
        return group_by(
            data_list,
            get_key_fn_list[0],
            item_fn=item_fn,
            tail_list_fn=tail_list_fn,
        )
    else:
        groups = group_by(data_list, get_key_fn_list[0])
        return {
            k: group_by_function_list(
                v,
                get_key_fn_list[1:],
                item_fn=item_fn,
                tail_list_fn=tail_list_fn,
            )
            for k, v in groups.items()
        }
