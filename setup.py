# setup.py

from setuptools import setup, find_packages

setup(
    name='real_time_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'boto3',
        's3fs',
        'satpy',
        'matplotlib'
    ],
)
