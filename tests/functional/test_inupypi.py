#!/usr/bin/env python
# -*- coding: utf8 -*-

import inupypi
import tempfile
import unittest

from tests.packages import *
from unipath import Path


class Test_Inupypi(unittest.TestCase):
    def setUp(self):
        self.app = inupypi.app.test_client()
        self.workspace = Path(tempfile.mkdtemp())
        self.packages = ['p1', 'p2', 'p3', 'p4']
        self.files = ['f1', 'f2', 'f3', 'f4']
        self.app.application.config['INUPYPI_REPO'] = self.workspace

    def tearDown(self):
        self.workspace.rmtree()

    def test_app_with_missing_package_dir(self):
        self.app.application.config['INUPYPI_REPO'] = Path(self.workspace, 'a')
        assert self.app.get('/').status_code == 500
        assert '500:' in self.app.get('/').data

    def test_app_without_packages(self):
        assert 'inetutils PyPI Server' in self.app.get('/').data
        assert 'Available Packages' not in self.app.get('/').data

    def test_app_with_package_folders(self):
        env_create_packages(self.workspace, self.packages)
        env_create_package_files(self.workspace, self.packages, self.files)
        assert 'inetutils PyPI Server' in self.app.get('/').data
        assert 'Available EggBaskets' in self.app.get('/').data

    def test_app_package(self):
        env_create_packages(self.workspace, self.packages)

        for p in self.packages:
            for f in self.files:
                page = self.app.get('/'+p+'/').data
                assert '404 - Page not found' not in page
                assert f not in page

        env_create_package_files(self.workspace, self.packages, self.files)

        for p in self.packages:
            for f in self.files:
                assert f in self.app.get('/test/'+p+'/').data

    def test_app_package_file(self):
        env_create_packages(self.workspace, self.packages)

        for p in self.packages:
            for f in self.files:
                response = self.app.get('/test/'+p+'/get/'+f)
                assert response.status_code == 404

        env_create_package_files(self.workspace, self.packages, self.files)

        for p in self.packages:
            for f in self.files:
                f = '%s.tar.gz' % f
                response = self.app.get('/test/'+p+'/get/'+f)
                assert response.status_code == 200
                assert response.content_type == 'application/x-tar'
                assert response.headers.get('Content-Disposition') == \
                        'attachment; filename=%s' % f
