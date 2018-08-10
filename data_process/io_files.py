import os
import glob


def file_list_in(root, pattern, **kwargs):
    pattern = os.path.join(root, pattern)
    rv = glob.glob(pattern, **kwargs)
    rv = [os.path.relpath(x, root) for x in rv]
    return rv
