#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from inupypi import __version__
from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


requirements = ['Flask', 'Flask-Themes', 'Flask-HTAuth', 'argparse', 'unipath']


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)

        self.test_args = ['-sv', '--pyargs', self.test_suite]

    def run_tests(self):
        import pytest

        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(cmdclass={'test': PyTest},
      description='A multiple repository PyPI server implementation',
      entry_points={'console_scripts': ['inupypi_server = inupypi:app']},
      include_package_data=True,
      install_requires=requirements,
      license='BSD',
      long_description=open("README.rst").read(),
      maintainer='Muhammad Hallaj Subery',
      maintainer_email='hallajs@gmail.com',
      name='inupypi',
      packages=find_packages(),
      platforms='FreeBSD, Linux',
      test_suite='tests',
      tests_require=['Flask-Testing', 'pytest'],
      url='https://github.com/hallaj/inupypi',
      version=__version__)
