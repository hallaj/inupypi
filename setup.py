#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

from setuptools import setup, find_packages

setup(
        name='inupypi',
        version='0.1',
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        test_suite='inupypi',
        install_requires=['Flask', 'pkgtools'],
        )
