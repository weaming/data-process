import copy
from decimal import Decimal


def is_float(value):
    if isinstance(value, (float, Decimal)):
        return True
    if isinstance(value, str):
        if all(x in '0123456789.' for x in value):
            return True
    return False


class DictIterator(object):
    def __init__(self, data: dict):
        self.data = copy.deepcopy(data)
        if hasattr(self, 'init') and callable(self.init):
            self.init()

    def transfer(self):
        return self._transfer_dict(self.data)

    def _transfer_dict(self, data: dict):
        for k, v in data.items():
            data[k] = self._transfer_value(v)
        return self.value_dict(data)

    def _transfer_value(self, v):
        if is_float(v):
            return self.value_float(v)
        if isinstance(v, int):
            return self.value_int(v)
        elif isinstance(v, str):
            return self.value_string(v)
        elif isinstance(v, list):
            rv = [self._transfer_value(x) for x in v]
            return self.value_list(rv)
        elif isinstance(v, dict):
            rv = self._transfer_dict(v)
            return self.value_dict(rv)
        else:
            raise Exception('unprocessed value: {}, type: {}'.format(v, type(v)))

    def value_list(self, v):
        return v

    def value_dict(self, v):
        return v

    def value_string(self, value):
        return value

    def value_float(self, value):
        return value

    def value_int(self, value):
        return value


class ObjectifyDict(dict):
    def __getattr__(self, item):
        if item in self:
            return self[item]


def get_fn_float(ndigit=2, decimal=True):
    def value_float(value):
        rv = ('{:.%sf}' % ndigit).format(Decimal(value))
        if decimal:
            return Decimal(rv)
        return rv

    return value_float


def replace_dict_keys(data, new_key_fn):
    return {new_key_fn(k): data[k] for k in data}


def test():
    class FixFloatDictIterator(DictIterator):
        def init(self):
            self.value_float = get_fn_float(ndigit=3, decimal=True)

        def value_dict(self, v):
            return ObjectifyDict(v)

    data = {
        'a': '3.0000000001',
        'b': ['4.243420004'],
        'c': {
            'cc': '34.00003',
            'cd': '32.23423423',
        },
    }

    iterator = FixFloatDictIterator(data)
    print(iterator.transfer())
    print(data)
