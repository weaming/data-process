from collections import defaultdict
from itertools import chain
from .group_by import group_by
from .iter_dict import replace_dict_keys


def get_count_in_list(lst, k):
    return sum(map(lambda x: 1 if x == k else 0, lst))


def get_unique_key(lst, key, prefix, force=False):
    if force or get_count_in_list(lst, key) > 1:
        return prefix + key
    return key


def _join(data_list_a, data_list_b, a_get_key, b_get_key, left=True, right=True, a_prefix='a.', b_prefix='b.',
          force=False):
    """
    condition: data's key is unique

    :param data_list_a:
    :param data_list_b:
    :param a_get_key:
    :param b_get_key:
    :param left:
    :param right:
    :return:
    """

    all_origin_fields = list(chain(data_list_a[0].keys(), data_list_b[0].keys()))
    a_groups = group_by(data_list_a, a_get_key)
    b_groups = group_by(data_list_b, b_get_key)
    
    # extract the only one data
    a_groups = {k: replace_dict_keys(a_groups[k][0], lambda k: get_unique_key(all_origin_fields, k, a_prefix, force)) for k in a_groups.keys()}
    b_groups = {k: replace_dict_keys(b_groups[k][0], lambda k: get_unique_key(all_origin_fields, k, b_prefix, force)) for k in b_groups.keys()}

    all_fields = chain(a_groups.keys(), b_groups.keys())

    rv = []
    for k in all_fields:
        a = a_groups.get(k)
        b = b_groups.get(k)

        data = defaultdict(lambda: None)
        rv.append(data)
        if a and left:
            data.update(a)
        if b and right:
            data.update(b)
    return rv


def left_join(a, b, a_get_key, b_get_key, **kwargs):
    return _join(a, b, a_get_key, b_get_key, left=True, right=False, **kwargs)


def right_join(a, b, a_get_key, b_get_key, **kwargs):
    return _join(a, b, a_get_key, b_get_key, left=False, right=True, **kwargs)


def inner_join(a, b, a_get_key, b_get_key, **kwargs):
    return _join(a, b, a_get_key, b_get_key, left=False, right=False, **kwargs)


def outer_join(a, b, a_get_key, b_get_key, **kwargs):
    return _join(a, b, a_get_key, b_get_key, left=True, right=True, **kwargs)
