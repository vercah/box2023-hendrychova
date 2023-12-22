import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "maw",
    version = "0.0.1",
    author = "Veronika Hendrychova, Nazar Misyats",
    description = ("Implementations of algorithms for Minimal Absent Words "
                   "in sets of sequences."),
    license = "MIT",
    keywords = "bioinformatics maw sequences",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['maw'],
    long_description=read('README.md'),
    entry_points={
        'console_scripts': [
            'maw = maw.main:main',
        ]
    }
)