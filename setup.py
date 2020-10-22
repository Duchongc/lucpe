#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 15:40
# @Author  : Anran
# @File    : setup.py
# @Function:

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="InterfaceUseCaseParameterExplosion", # Replace with your own username
    version="0.0.1",
    author="Anran",
    author_email="1978529954@qq.com",
    description="InterfaceUseCaseParameterExplosion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)