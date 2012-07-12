#!/usr/bin/env python
# -*- coding: utf8 -*-

import tempfile
import unittest

from inupypi import app
from inupypi.components.packages import *
from tests.packages import *
from unipath import Path


class Test_Packages(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.workspace = Path(tempfile.mkdtemp())
        self.packages = ['p1', 'p2', 'p3', 'p4']
        self.files = ['f1', 'f2', 'f3', 'f4']
        self.files.sort(reverse=True)

        self.app.application.config['PACKAGE_PATH'] = self.workspace

    def tearDown(self):
        self.workspace.rmtree()

    def test_get_packages_without_packages_folder(self):
        self.app.application.config['PACKAGE_PATH'] = Path(self.workspace, 'a')

        try:
            get_packages()
            return False
        except:
            return True

    def test_get_packages(self):
        assert get_packages() == []

        env_create_packages(self.workspace, self.packages)
        env_create_package_files(self.workspace, self.packages, self.files)
        created_packages = [Path(self.workspace, package)
                for package in self.packages]
        packages = [p.filepath for p in get_packages()]

        assert created_packages == packages

    def test_get_packages_from_folders_only(self):
        assert get_packages() == []

        env_create_packages(self.workspace, self.packages)
        env_create_package_files(self.workspace, self.packages, self.files)

        packages_and_files = sorted([Path(package)
                for package in self.packages + self.files])

        created_packages = [Path(self.workspace, package)
                for package in self.packages]
        packages = [p.filepath for p in get_packages()]

        assert get_packages() != packages_and_files
        assert created_packages == packages

    def test_get_package_files(self):
        env_create_packages(self.workspace, self.packages)

        for p in self.packages:
            assert get_package_files(p) == []

        env_create_package_files(self.workspace, self.packages, self.files)

        for p in self.packages:
            files = sorted([Path(self.workspace, p, '%s.tar.gz' % f)
                    for f in self.files])
            package_files = sorted([pkg.filepath
                for pkg in get_package_files(p)])
            assert package_files == files

    def test_get_current_package(self):
        env_create_packages(self.workspace, self.packages)
        env_create_package_files(self.workspace, self.packages, self.files)

        for p in self.packages:
            created_packages = Path(self.workspace, p, '%s.tar.gz' %
                    sorted(self.files, reverse=True)[0])
            assert get_current_package(p) == created_packages

    def test_get_file(self):
        for p in self.packages:
            for f in self.files:
                assert get_file(p, f) == False

        env_create_package_files(self.workspace, self.packages, self.files)

        for p in self.packages:
            for f in self.files:
                f = '%s.tar.gz' % f
                assert get_file(p, f) == Path(self.workspace, p, f)
