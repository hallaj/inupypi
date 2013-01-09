#!/usr/bin/env python
# -*- coding: utf8 -*-

import inupypi
import pytest
import unittest


class Test_Dirs(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def create_workspace(self, tmpdir):
        self.temp = tmpdir
        self.core_dirs = inupypi.core.Dirs(self.temp.strpath)
        self.dirs = ['dir1', 'dir2', 'dir3', 'dir4']

    def test_class_instance(self):
        self.assertIsInstance(self.core_dirs, inupypi.core.Dirs)
        self.assertEqual(self.core_dirs.__parents__, self.temp.strpath)

    def test_dir_contents(self):
        self.assertEqual([], self.core_dirs.__contents__)

        for dir_ in self.dirs:
            self.temp.join(dir_).mkdir()
            self.core_dirs = inupypi.core.Dirs(self.temp.strpath)
            self.assertEqual(self.core_dirs.__parents__, self.temp.strpath)
            self.assertIn(dir_, self.core_dirs.__contents__)
