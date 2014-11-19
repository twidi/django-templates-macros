#!/usr/bin/env python

from os.path import abspath, dirname, join
from setuptools import setup, find_packages


def read_relative_file(filename):
    """Returns contents of the given file, which path is supposed relative
    to this module."""
    with open(join(dirname(abspath(__file__)), filename)) as f:
        return f.read()


version = read_relative_file('VERSION').strip()
readme = read_relative_file('README.rst')

setup(
    name="django-templates-macros",
    version=version,
    license="MIT",
    description="Add macros to your django templates",
    long_description=readme,
    url="https://github.com/twidi/django-templates-macros",
    author='Stephane "Twidi" Angel',
    author_email="s.angel@twidi.com",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ]
)
