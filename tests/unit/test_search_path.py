#!/usr/bin/env python
# -*- coding: utf8 -*-

import inupypi


def test_search_path(tmpdir):
    dirs = ['dir1', 'dir2', 'dir3', 'dir4']

    for d in dirs:
        d = tmpdir.join(d)
        d.mkdir()

        assert inupypi.core.search_path(d.strpath.upper(),
                                        tmpdir.strpath) == d.strpath
