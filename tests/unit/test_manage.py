##!/usr/bin/env python
## -*- coding: utf8 -*-
#
#import tempfile
#import unittest
#
#from inupypi.components.packages import *
#from inupypi.components.packages.manage import *
#from tests.packages import *
#from unipath import Path
#from werkzeug import FileStorage
#
#
#class Test_Manage(unittest.TestCase):
#    def setUp(self):
#        self.app = app.test_client()
#        self.workspace = Path(tempfile.mkdtemp())
#        self.tmp_workspace = Path(tempfile.mkdtemp())
#        self.packages = ['p1', 'p2', 'p3', 'p4']
#        self.files = sorted(['f1', 'f2', 'f3', 'f4'], reverse=True)
#
#        self.app.application.config['PACKAGE_PATH'] = self.workspace
#
#    def tearDown(self):
#        self.workspace.rmtree()
#        self.tmp_workspace.rmtree()
#
#    def test_upload_package(self):
#        assert get_packages() == []
#
#        env_create_package_files(self.tmp_workspace, self.packages, self.files)
#
#        for p in self.packages:
#            for f in self.files:
#                filename = u'%s.tar.gz' % f
#                stream = open(Path(self.tmp_workspace, p, filename))
#                fs = FileStorage(filename=filename, stream=stream)
#                upload_package(fs)
#        packages = [p.filepath for p in get_packages()]
#        created_packages = [Path(self.workspace, package)
#                for package in self.packages]
#        assert packages == created_packages
#
#        for p in self.packages:
#            files = sorted([Path(self.workspace, p, '%s.tar.gz' % f)
#                    for f in self.files])
#            package_files = sorted([pkg.filepath
#                for pkg in get_package_files(p)])
#            assert files == package_files
