from collections import defaultdict


def group_by(data_list, get_group_key):
    groups = defaultdict(list)
    for x in data_list:
        key = get_group_key(x)
        groups[key].append(x)
    return groups
