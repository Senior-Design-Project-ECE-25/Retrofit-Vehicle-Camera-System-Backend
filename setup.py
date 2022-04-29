import os
from enum import Enum
from typing import List, Union
from setuptools import setup, find_packages

BASE_PATH = os.path.abspath(os.path.dirname(__file__))


class Env(Enum):
    """The valid environment values"""
    prod = 'prod'
    stage = 'stage'
    dev = 'dev'

    @classmethod
    def get_environment(cls, env_variable: str):
        try:
            environment = os.environ[env_variable].lower()
            return Env[environment]
        except KeyError:
            return cls.stage


def _read_readme() -> Union[str, None]:
    """Read the readme as a string"""
    try:
        with open(os.path.join(BASE_PATH, 'README.md'), 'r') as readme_file:
            return readme_file.read()
    except FileNotFoundError:
        return None


def _read_requirements(env=Env.stage) -> Union[List[str], None]:
    """Read the requriements as a list of required values"""
    requirements = os.path.join('requirements', f'{env.value}.txt')
    try:
        with open(os.path.join(BASE_PATH, requirements), 'r') as req_file:
            return [line.strip() for line in req_file]
    except FileNotFoundError:
        return None


def _get_version() -> str:
    """Get the version string from inside the module"""
    from rvcs import __version__
    return __version__


environment = Env.get_environment('RVCS_ENV')


setup(
    name='rvcs',
    version=_get_version(),
    description='API for exposing RVCS backend',
    long_description=_read_readme(),
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
    install_requires=_read_requirements(environment)
)
