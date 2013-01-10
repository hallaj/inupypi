#!/usr/bin/env python
# -*- coding: utf8 -*-

from setuptools import setup, find_packages

setup(name='inupypi',
      version='0.2.6.4',
      packages=find_packages(),
      url="https://github.com/hallaj/inupypi",
      long_description=open("README.md").read() + open("CHANGELOG.txt").read(),
      maintainer='Muhammad Hallaj Subery',
      maintainer_email='hallajs@gmail.com',
      license="BSD",
      description="A PyPiServer based on the Flask Framework and supports \
multiple repositories.",
      platforms='Linux, FreeBSD',
      include_package_data=True,
      zip_safe=False,
      test_suite='tests',
      install_requires=['Flask', 'Flask-Assets', 'argparse', 'cssmin',
                        'pkgtools', 'unipath'],
      scripts=['inupypi_server', 'inupypi_configure.py'],
      package_data={'conf_samples': ['httpd-inupypi.conf.sample']})
