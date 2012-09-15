#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

from setuptools import setup, find_packages

setup(
        name='inupypi',
        version='0.2.5.2',
        packages=find_packages(),
        long_description=open("README.rst").read(),
        maintainer='Hallaj Subery',
        maintainer_email='hallajs@gmail.com',
        license="BSD",
        description='A PyPiServer based on the Flask Framework',
        platform='Linux,FreeBSD',
        include_package_data=True,
        zip_safe=False,
        test_suite='tests',
        install_requires=['Flask', 'Flask-Assets', 'cssmin', 'pkgtools',
            'unipath']
        )
