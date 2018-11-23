# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import re
from os import path
from io import open

here = path.abspath(path.dirname(__file__))


def _read(fname):
    if path.isfile(fname):
        with open(path.join(here, fname), encoding="utf-8") as f:
            return f.read()
    else:
        print("warning: file {} does not exist".format(fname))
        return ""


def get_version(path):
    src = _read(path)
    pat = re.compile(r"""^version = ['"](.+?)['"]$""", re.MULTILINE)
    result = pat.search(src)
    version = result.group(1)
    return version


long_description = _read("README.md")
install_requires = [
    l
    for l in _read("requirements.txt").split("\n")
    if l.strip() and not l.strip().startswith("#")
]

name = "data-process"
gh_repo = "https://github.com/weaming/{}".format(name)
version = get_version("data_process/__init__.py")

setup(
    name=name,  # Required
    version=version,  # Required
    description="make processing 2d data more convenient",  # Required
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url=gh_repo,  # Optional
    author="weaming",  # Optional
    author_email="garden.yuen@gmail.com",  # Optional
    packages=find_packages(exclude=["contrib", "docs", "tests"]),  # Required
    keywords="json csv pandas",  # Optional
    entry_points={},  # Optional
    install_requires=install_requires,
    project_urls={"Bug Reports": gh_repo, "Source": gh_repo},  # Optional
)
