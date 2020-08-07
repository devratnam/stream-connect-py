# -*- coding: utf-8 -*-
import sys
from os.path import join, dirname
from setuptools import setup, find_packages

VERSION = (1, 0, 7)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

f = open(join(dirname(__file__), 'README.md'))
long_description = f.read().strip()
f.close()

install_requires = [
    "confluent-kafka==0.11.6"
]


setup(
    name = "stream-connect",
    description = "Python library to connect streaming service",
    url = "https://github.com/devratnam/stream-connect-py",
    long_description = long_description,
    version = __versionstr__,
    author = "Devendra Ratnam",
    author_email = "ratnam747@gmail.com",
    packages=['stream_connect', 'stream_connect.services'],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    install_requires=install_requires,
)
