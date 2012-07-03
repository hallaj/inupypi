#!/usr/bin/env python
# -*- coding: utf8 -*-

import inupypi
import shutil
import tempfile
import unittest

from inupypi.components.packages import get_packages, get_package_files, \
        get_file, get_latest_file
from inupypi.components.packages import PackageInfo
from unipath import Path


class Test_Packages(unittest.TestCase):
    def create_packages(self):
        packages = []

        for package in self.packages:
            package = Path(self.workspace, package)
            package.mkdir()
            packages.append(package)
        self.packages = packages

    def create_package_files(self):
        for package in self.packages:
            for f in self.package_files:
                Path(self.workspace, package).mkdir()
                Path(self.workspace, package, f).write_file(f)

    def setUp(self):
        self.workspace = tempfile.mkdtemp()

        self.app = inupypi.app.test_client()
        self.app.application.config['PKG_PATH'] = self.workspace

        self.packages = ['package_a', 'package_b', 'package_c']
        self.package_files = ['file-1.0', 'file-2.0']
        self.packages.sort()

    def tearDown(self):
        shutil.rmtree(self.workspace)

    def test_get_packages(self):
        assert get_packages() == []

        self.create_packages()
        package_file = Path(self.workspace, 'some_file')
        package_file.write_file(package_file)

        get_packages_items = [package.package for package in get_packages()]

        assert get_packages_items == self.packages
        assert package_file not in get_packages_items

    def test_get_package_files(self):
        for package in self.packages:
            assert get_package_files(package) == []

        self.create_packages()
        self.create_package_files()

        for package in self.packages:
            package_files = [Path(self.workspace, package, f)
                    for f in self.package_files]
            package_files.sort(reverse=True)
            assert get_package_files(package) == package_files

    def test_get_package(self):
        for package in self.packages:
            for f in self.package_files:
                assert get_file(package, f) == False

        self.create_package_files()

        for package in self.packages:
            for f in self.package_files:
                assert get_file(package, f) == Path(self.workspace, package, f)

    def test_get_latest_file(self):
        self.create_package_files()

        for package in self.packages:
            assert get_latest_file(package) == self.package_files[-1:][0]

if __name__ == '__main__':
    unittest.main()
