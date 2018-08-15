from collections import defaultdict
from itertools import chain
from .group_by import group_by


def _join(data_list_a, data_list_b, a_get_key, b_get_key, left=True, right=True):
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

    a_groups = group_by(data_list_a, a_get_key)
    b_groups = group_by(data_list_b, b_get_key)

    # extract the only one data
    a_groups = {k: a_groups[k][0] for k in a_groups.keys()}
    b_groups = {k: b_groups[k][0] for k in b_groups.keys()}

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


def left_join(a, b, a_get_key, b_get_key):
    return _join(a, b, a_get_key, b_get_key, left=True, right=False)


def right_join(a, b, a_get_key, b_get_key):
    return _join(a, b, a_get_key, b_get_key, left=False, right=True)


def inner_join(a, b, a_get_key, b_get_key):
    return _join(a, b, a_get_key, b_get_key, left=False, right=False)


def outer_join(a, b, a_get_key, b_get_key):
    return _join(a, b, a_get_key, b_get_key, left=True, right=True)
