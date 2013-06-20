#!/usr/bin/env python
# -*- coding: utf8 -*-

import inupypi
import pytest


class Test_Dirs(object):
    @pytest.fixture(autouse=True)
    def create_workspace(self, tmpdir):
        self.temp = tmpdir
        self.core_dirs = inupypi.core.Dirs(self.temp.strpath)
        self.dirs = ['dir1', 'dir2', 'dir3', 'dir4']
        self.abs_dirs = [tmpdir.join(dir) for dir in
                         self.dirs]

    def test_class_instance(self):
        assert(isinstance(self.core_dirs, inupypi.core.Dirs))
        assert(self.core_dirs.__parents__ == self.temp.strpath)

    def test_dir_contents(self):
        assert(not self.core_dirs.__contents__)

        for dir_ in self.dirs:
            self.temp.join(dir_).mkdir()
            self.core_dirs = inupypi.core.Dirs(self.temp.strpath)

            assert(self.core_dirs.__parents__ == self.temp.strpath)
        for dir_ in self.abs_dirs:
            assert(dir_ in self.core_dirs.__contents__)
