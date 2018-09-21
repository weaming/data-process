# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

name = 'data-process'
gh_repo = 'https://github.com/weaming/{}'.format(name)
version = '0.1.33'

setup(
    name=name,  # Required

    version=version,  # Required

    # This is a one-line description or tagline of what your project does.
    description='make processing 2d data more convenient',  # Required
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)

    url=gh_repo,  # Optional
    author='weaming',  # Optional
    author_email='garden.yuen@gmail.com',  # Optional

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required

    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a string of words separated by whitespace, not a list.
    keywords='json csv pandas',  # Optional

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={  # Optional
    },

    project_urls={  # Optional
        'Bug Reports': gh_repo,
        'Source': gh_repo,
    },
    )
