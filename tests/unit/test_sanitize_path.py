#!/usr/bin/env python
# -*- coding: utf8 -*-

from inupypi.core import sanitize_path


def test_sanitize_path():
    assert sanitize_path('/tmp') == 'tmp'
