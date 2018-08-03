import os
import glob


def file_list_in(root, pattern, **kwargs):
    cwd = os.getcwd()
    os.chdir(root)
    rv = glob.glob(pattern, **kwargs)
    os.chdir(cwd)
    return rv
