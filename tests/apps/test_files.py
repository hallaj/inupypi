#!/usr/bin/env python
# -*- coding: utf8 -*-

import flask.ext.testing
import inupypi
import pytest


class Test_Files(flask.ext.testing.TestCase):
    @pytest.fixture(autouse=True)
    def create_workspace(self, tmpdir):
        self.temp = tmpdir

    def create_app(self):
        app = inupypi.create_app()
        app.config['TESTING'] = True
        app.config['INUPYPI_REPO'] = str(self.temp)
        return app

    def test_missing_file(self):
        test_file = self.temp.join('file_a.txt')
        resp = self.client.get('/%s' % test_file.basename,
                               follow_redirects=True)

        assert resp.status_code == 404
        assert 'Path or File could not be found!' in resp.data

    def test_file_exists(self):
        repo = 'repo1'
        data = 'file content'

        test_repo = self.temp.join(repo).mkdir()
        test_file = test_repo.join('file_a.txt')
        test_file.write(data)
        resp = self.client.get('/%s/%s' % (repo.upper(),
                                           test_file.basename),
                               follow_redirects=True)
        content = resp.headers.get('Content-Disposition')

        assert resp.status_code == 200
        assert content == 'attachment; filename=%s' % test_file.basename
        assert data in resp.data
