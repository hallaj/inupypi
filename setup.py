#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)

        self.test_args = ['-sv', '--pyargs', self.test_suite]

    def run_tests(self):
        import pytest

        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name='inupypi',
    version='0.3.3',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/hallaj/inupypi',
    maintainer='Muhammad Hallaj Subery',
    maintainer_email='hallajs@gmail.com',
    license='BSD',
    description='A multiple repository PyPI server implementation',
    long_description=open("README.rst").read(),
    platforms='FreeBSD, Linux',
    test_suite='tests',
    tests_require=['Flask-Testing', 'pytest'],
    cmdclass={'test': PyTest},
    entry_points={'console_scripts': ['inupypi_server = inupypi:app']},
    install_requires=['Flask', 'Flask-Themes', 'Flask-HTAuth', 'argparse',
                      'unipath'])
