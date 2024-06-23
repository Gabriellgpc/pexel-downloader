# -*- coding: utf-8 -*-
# @Author: Luis Condados
# @Last Modified by:   Luis Condados
from setuptools import setup, find_packages

setup(
    name='pexel_downloader',
    version='0.3.1',
    packages=find_packages(),
    install_requires=[
        "requests",
        "joblib",
        "tqdm"
    ],
    author='Luis Condados',
    author_email='condadoslgpc@gmail.com',
    description='A package for downloading images from Pexels.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Gabriellgpc/pexel-downloader',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
