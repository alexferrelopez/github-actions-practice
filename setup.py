# setup.py
from setuptools import setup, find_packages

setup(
    name="mypkg",
    version="0.1.0",
    description="Demo package that works on Python 2.7 and 3.x",
    packages=find_packages(exclude=("tests", "tests.*")),
    # Don't set python_requires here if you still want to install on Py2.7
    # python_requires=">=2.7",  # optional, but older setuptools may ignore it
)
