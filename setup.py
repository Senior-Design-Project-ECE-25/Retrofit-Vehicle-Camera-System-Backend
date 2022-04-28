import os
from enum import Enum
from typing import List, Union
from setuptools import setup, find_packages


class Env(Enum):
    PROD = 'prod'
    STAGE = 'stage'
    DEV = 'dev'


def read_readme() -> Union[str, None]:
    from rvcs.config import BASE_PATH
    try:
        with open(os.path.join(BASE_PATH, 'README.md'), 'r') as readme_file:
            return readme_file.read()
    except FileNotFoundError:
        return None


def read_requirements(env=Env.PROD) -> Union[List[str], None]:
    from rvcs.config import BASE_PATH
    requirements = os.path.join('requirements', f'{env.value}.txt')
    try:
        with open(os.path.join(BASE_PATH, requirements), 'r') as req_file:
            return [line.strip() for line in req_file]
    except FileNotFoundError:
        return None


def get_version() -> str:
    from rvcs import __version__
    return __version__


setup(
    name='rvcs',
    version=get_version(),
    description='API for exposing RVCS backend',
    long_description=read_readme(),
    author='Jack McVeigh',
    author_email='jmcveigh55@gmail.com',
    url='https://github.com/Senior-Design-Project-ECE-25'
        '/Retrofit-Vehicle-Camera-System-Backend.git',
    python_requires='>=3.7.3',
    packages=find_packages(),
    package_data={
        'rvcs': [
            'config/conf.json',
            'config/logger.ini'
        ]
    },
    entry_points={
        'console_scripts': [
            'rvcs=rvcs.cli:entry_point',
        ],
    },
    install_requires=read_requirements(Env.PROD)
)
