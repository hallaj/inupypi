#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

from setuptools import setup, find_packages

setup(
        name='inupypi',
        version='0.2.3',
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        test_suite='tests',
        install_requires=['Flask', 'Flask-Assets', 'cssmin', 'pkgtools',
            'unipath']
        )
