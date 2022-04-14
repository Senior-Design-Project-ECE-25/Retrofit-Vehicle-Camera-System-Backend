from setuptools import setup, find_packages


setup(
    name='rvcs',
    version='0.0.0',
    description='API for exposing RVCS backend',
    author='Jack McVeigh',
    author_email='jmcveigh55@gmail.com',
    url='https://github.com/Senior-Design-Project-ECE-25'
        '/Retrofit-Vehicle-Camera-System-Backend.git',
    packages=find_packages(),
    package_data={
        'rvcs': ['config/conf.json', 'config/logger.ini']
    },
    entry_points={
        'console_scripts': [
            'rvcs=rvcs.app:main',
        ],
    }
)
