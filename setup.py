from setuptools import setup, find_packages
from pathlib import Path

PYTHON_VERSION_REQ = ">3.8.0"
CURRENT_DIRECTORY = Path(__file__).parent.absolute()

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    require = [x.strip() for x in f.readlines()]


def read(rel_path):
    here = Path(__file__).parent.absolute()
    with open(here.joinpath(rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name="iblrig",
    version=get_version(Path("iblrig").joinpath("__init__.py")),
    python_requires=PYTHON_VERSION_REQ,
    description="IBL libraries",
    license="MIT",
    long_description=long_description,
    author="IBL Staff",
    url="https://www.internationalbrainlab.com/",
    packages=find_packages(exclude=["scratch"]),  # same as name
    # external packages as dependencies
    install_requires=require,
    scripts=[],
)
