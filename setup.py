#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

from setuptools import setup, find_packages

setup(
        name='inupypi',
        version='0.2.5.6',
        packages=find_packages(),
        url="https://github.com/hallaj/inupypi",
        long_description=open("README.rst").read(),
        maintainer='Muhammad Hallaj Subery',
        maintainer_email='hallajs@gmail.com',
        license="BSD",
        description="A PyPiServer based on the Flask Framework and supports \
multiple repositories.",
        platform='Linux, FreeBSD',
        include_package_data=True,
        zip_safe=False,
        test_suite='tests',
        install_requires=['Flask', 'Flask-Assets', 'argparse', 'cssmin',
            'pkgtools', 'unipath']
        )
