# -*- coding: utf-8 -*
"""
Setup script for behave.

USAGE:
    python setup.py install
    python setup.py behave_test     # -- XFAIL on Windows (currently).
    python setup.py nosetests

REQUIRES:
* setuptools >= 36.2.0

SEE ALSO:
* https://setuptools.readthedocs.io/en/latest/history.html
"""

import sys
import os.path

from setuptools import find_packages, setup
from setuptools_behave import behave_test

HERE0 = os.path.dirname(__file__) or os.curdir
os.chdir(HERE0)
HERE = os.curdir
sys.path.insert(0, HERE)


# -----------------------------------------------------------------------------
# CONFIGURATION:
# -----------------------------------------------------------------------------
python_version = float("%s.%s" % sys.version_info[:2])
BEHAVE = os.path.join(HERE, "behave")
README = os.path.join(HERE, "README.rst")
description = "".join(open(README).readlines()[4:])


# -----------------------------------------------------------------------------
# UTILITY:
# -----------------------------------------------------------------------------
def find_packages_by_root_package(where):
    """
    Better than excluding everything that is not needed,
    collect only what is needed.
    """
    root_package = os.path.basename(where)
    packages = ["%s.%s" % (root_package, sub_package)
                for sub_package in find_packages(where)]
    packages.insert(0, root_package)
    return packages


# -----------------------------------------------------------------------------
# SETUP:
# -----------------------------------------------------------------------------
setup(
    name="behave-auto-mock",
    version="0.0.4",
    description="BDD with behave and mocks",
    long_description=description,
    author="Chris Ramacciotti",
    author_email="chris.j.rama@gmail.com",
    url="http://github.com/christherama/behave-auto-mock",
    provides=["behave", "setuptools_behave"],
    packages=find_packages_by_root_package(BEHAVE),
    py_modules=["setuptools_behave"],
    entry_points={
        "console_scripts": [
            "behave = behave.__main__:main"
        ],
        "distutils.commands": [
            "behave_test = setuptools_behave:behave_test"
        ]
    },
    # -- REQUIREMENTS:
    # SUPPORT: python2.7, python3.3 (or higher)
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*",
    install_requires=[
        "cucumber-tag-expressions >= 1.1.1",
        "parse >= 1.8.2",
        "parse_type >= 0.4.2",
        "six >= 1.12.0",
        "traceback2; python_version < '3.0'",
        "enum34; python_version < '3.4'",
        # -- PREPARED:
        "win_unicode_console; python_version < '3.6'",
        "colorama",
        "mock >= 2.0",
    ],
    test_suite="nose.collector",
    tests_require=[
        "pytest >= 3.0",
        "pytest-html >= 1.19.0",
        "nose >= 1.3",
        "mock >= 1.1",
        "PyHamcrest >= 1.8",
        "path.py >= 11.5.0"
    ],
    cmdclass={
        "behave_test": behave_test,
    },
    extras_require={
        "docs": [
            "sphinx >= 1.6",
            "sphinx_bootstrap_theme >= 0.6"
        ],
        "develop": [
            "coverage",
            "pytest >= 3.0",
            "pytest-html >= 1.19.0",
            "pytest-cov",
            "tox",
            "invoke >= 1.2.0",
            "path.py >= 11.5.0",
            "pycmd",
            "pathlib; python_version <= '3.4'",
            "modernize >= 0.5",
            "pylint",
        ],
    },
    # MAYBE-DISABLE: use_2to3
    use_2to3=bool(python_version >= 3.0),
    license="BSD",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: BSD License",
    ],
    zip_safe=True,
)
