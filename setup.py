import re
from setuptools import setup, find_namespace_packages


name = 'desc_bpz'


def read_value(value, file=f'{name}/__init__.py'):
    version_file = open(file).read()
    version_match = re.search(
        rf"^{value} = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


packages = find_namespace_packages()
setup(
    name=name,
    version=read_value('__version__'),
    author="Narciso Benitez, Dan Coe, Will Hartley,"
        "Sam Schmidt, LSST DESC PZWG",
    author_email="fake@fake.edu",
    packages=packages,
    scripts=['scripts/bpz.py'],
    package_data={
        "": ["*.h5", "*.yaml", "*.sed", "*.res",
             "*.AB", "*.columns", "*.pars"],
        "tests": ["*.h5", "*.yaml"],
        "SED": ["*.sed"],
        "FILTER": ["*.res"],
        "AB": ["*.AB"],
        "scripts": ["*.columns, *.pars"]
    },
    include_package_data=True,
    license="BSD 3-Clause License",
    description="Python3 version of BPZ used in DESC",
    url="https://github.com/LSSTDESC/DESC_BPZ",
    long_description=open("README.md").read(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD 3-Clause",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
        ],
    install_requires=['numpy',
                      'scipy',
                      'pandas>=1.1',
                      'h5py',
                      'tables',
                      'icecream',
                      ],
    python_requires='>=3.5',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
