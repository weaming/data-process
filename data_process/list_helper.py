def flat_list(data):
    rv = []
    for x in data:
        if isinstance(x, (tuple, list)):
            rv += flat_list(data)
        else:
            rv.append(x)
    return rv
