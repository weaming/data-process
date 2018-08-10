import os
import glob


def file_list_in(root, pattern, **kwargs):
    if root[-1] != '/':
        root += '/'
    pattern = root + pattern
    print(pattern)
    rv = glob.glob(pattern, **kwargs)
    rv = [x[len(root):] for x in rv]
    return rv
