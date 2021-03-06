#!/usr/bin/env python
# -*- coding: utf8 -*-

import flask.ext.testing
import pytest

from inupypi import __version__
from inupypi.__main__ import create_app


class Test_Basic(flask.ext.testing.TestCase):
    @pytest.fixture(autouse=True)
    def create_workspace(self, tmpdir):
        self.temp = tmpdir

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['INUPYPI_REPO'] = str(self.temp)
        return app

    def test_index(self):
        resp = self.client.get('/')

        assert resp.status_code == 200
        assert '<table' in resp.data
        assert __version__ in resp.data

    def test_about(self):
        resp = self.client.get('/about/')

        assert resp.status_code == 200
        assert 'About inupypi', resp.data
