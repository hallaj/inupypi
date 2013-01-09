#!/usr/bin/env python
# -*- coding: utf8 -*-

import inupypi


def test_sanitize_path():
    assert(inupypi.core.sanitize_path('/tmp') == 'tmp')
