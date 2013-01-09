#!/usr/bin/env python
# -*- coding: utf8 -*-

import flask.ext.testing
import inupypi
import pytest

from StringIO import StringIO


class Test_Repo(flask.ext.testing.TestCase):
    @pytest.fixture(autouse=True)
    def create_workspace(self, tmpdir):
        self.temp = tmpdir

    def create_app(self):
        app = inupypi.create_app()
        app.config['TESTING'] = True
        app.config['INUPYPI_REPO'] = str(self.temp)
        return app

    def test_missing_repo_path(self):
        self.temp.remove()
        resp = self.client.get('/')

        self.assertEqual(500, resp.status_code)
        self.assertIn('500: Internal Server Error', resp.data)
        self.assertIn('Missing repository or package path!', resp.data)

    def test_empty_repo(self):
        repo = self.temp.join('repo')

        main_resp = self.client.get('/')
        repo_resp = self.client.get('/%s/' % repo.basename)

        self.assertEqual(200, main_resp.status_code)
        self.assertEqual(404, repo_resp.status_code)
        self.assertIn('Path or File could not be found!', repo_resp.data)
        self.assertNotIn('%s</a>' % repo.basename, main_resp.data)

    def test_repo_exists(self):
        repo = self.temp.join('repo1').mkdir()
        self.create_app()

        main_resp = self.client.get('/')
        repo_resp = self.client.get('/%s/' % repo.basename)

        self.assertEqual(200, main_resp.status_code)
        self.assertEqual(200, repo_resp.status_code)
        self.assertIn('%s</a>' % repo.basename, main_resp.data)

    def test_create_path(self):
        main_repo = self.temp.join('repo1')
        sub_repo = main_repo.join('sub_repo1')
        resp = self.client.get('/')

        self.assertEqual(200, resp.status_code)
        self.assertNotIn(main_repo.basename, resp.data)

        resp = self.client.post('/admin/create_folder/',
                                data={'folder_name': main_repo.basename},
                                follow_redirects=True)
        self.assertEqual(200, resp.status_code)
        self.assertTrue(main_repo.check(dir=True))

        resp = self.client.post('/admin/create_folder/',
                                data={'folder_name': '%s/%s' %
                                      (main_repo.basename, sub_repo.basename)},
                                follow_redirects=True)
        self.assertEqual(200, resp.status_code)
        self.assertTrue(sub_repo.check(dir=True))

        resp = self.client.get('/%s/' % main_repo.basename)

        self.assertEqual(200, resp.status_code)
        self.assertIn(sub_repo.basename, resp.data)

    def test_rename_path(self):
        repo = self.temp.join('repo1').mkdir()
        repo_rename = self.temp.join('repo2')

        resp = self.client.get('/')

        self.assertEqual(200, resp.status_code)
        self.assertIn(repo.basename, resp.data)

        resp = self.client.post('/admin/rename/', data={'current':
                                repo.basename, 'rename': repo_rename.basename},
                                follow_redirects=True)

        self.assertEqual(200, resp.status_code)
        self.assertFalse(repo.check(dir=True))

        resp = self.client.get('/')

        self.assertEqual(200, resp.status_code)
        self.assertIn(repo_rename.basename, resp.data)
        self.assertNotIn(repo.basename, resp.data)

    def test_remove_path(self):
        repo = self.temp.join('repo1').mkdir()
        resp = self.client.get('/')

        self.assertEqual(200, resp.status_code)
        self.assertIn(repo.basename, resp.data)

        resp = self.client.post('/admin/remove/', data={'item_path':
                                                        repo.basename},
                                follow_redirects=True)

        self.assertEqual(200, resp.status_code)
        self.assertFalse(repo.check(dir=True))

    def test_upload_file(self):
        repo = self.temp.join('repo').mkdir()
        upload_file = repo.join('uploaded_file.txt')

        self.assertFalse(upload_file.check(file=True))
        resp = self.client.post('/admin/upload/',
                                data={'path': repo.basename,
                                      'file': (StringIO('File upload content'),
                                               upload_file.basename)},
                                follow_redirects=True)
        self.assertEqual(200, resp.status_code)
        self.assertTrue(upload_file.check(file=True))

        resp = self.client.get('/%s/' % repo.basename)
        self.assertIn(upload_file.basename, resp.data)
