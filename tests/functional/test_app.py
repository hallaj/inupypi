#!/usr/bin/env python
# -*- coding: utf8 -*-

import inupypi
import shutil
import tempfile
import unittest

from inupypi.components.packages import get_packages
from unipath import Path


class Test_Inupypi(unittest.TestCase):
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

    def test_empty_application(self):
        app = self.app.get('/')
        assert 'inetutils PyPI' in app.data


    def test_get_folders(self):
        assert get_packages() == []

        for package in self.packages:
            assert package not in self.app.get('/').data

        self.create_packages()

        for package in self.packages:
            assert package.name in self.app.get('/').data

        assert get_packages() == self.packages

    def test_get_package_files(self):
        for package in self.packages:
            for f in self.package_files:
                assert f not in self.app.get('/package/'+package+'/').data

        self.create_package_files()

        for package in self.packages:
            for f in self.package_files:
                assert f in self.app.get('/package/'+package+'/').data

    def test_get_package(self):
        for package in self.packages:
            for f in self.package_files:
                app = self.app.get('/package/'+package+'/get/'+f)
                assert app.status_code == 404

        self.create_package_files()

        for package in self.packages:
            for f in self.package_files:
                app = self.app.get('/package/'+package+'/get/'+f)
                assert app.status_code == 200
                assert app.content_type == 'application/octet-stream'

if __name__ == '__main__':
    unittest.main()
