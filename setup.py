import os
from setuptools import setup, find_packages

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

setup(
    name = "osisaf_thredds_download",
    version = "0.0.0",
    author = "Johannes Lohse",
    author_email = "johannes.lohse@utas.edu.au",
    description = ("Download netCDF files from OSISAF thredds server."),
    license = "The Ask Johannes Before You Do Anything License",
    long_description=read('README.md'),
    install_requires = [
        'pathlib',
        'loguru',
        'xarray',
        'requests',
        'bs4',
    ],
    packages = find_packages(where='src'),
    package_dir = {'': 'src'},
)
