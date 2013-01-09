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

        self.assertEqual(404, resp.status_code)
        self.assertIn('Path or File could not be found!', resp.data)

    def test_file_exists(self):
        test_data = 'file content'
        test_repo = self.temp.join('repo1').mkdir()
        test_file = test_repo.join('file_a.txt')
        test_file.write(test_data)
        resp = self.client.get('/%s/%s' % (test_repo.basename,
                                           test_file.basename),
                               follow_redirects=True)

        self.assertEqual(200, resp.status_code)
        self.assertEqual(resp.headers.get('Content-Disposition'),
                         'attachment; filename=%s' % test_file.basename)
        self.assertEqual(resp.data, test_data)
