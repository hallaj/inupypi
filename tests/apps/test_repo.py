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

        assert(500 == resp.status_code)
        assert('500: Internal Server Error' in resp.data)
        assert('Missing repository or package path!' in resp.data)

    def test_empty_repo(self):
        repo = self.temp.join('repo')

        main_resp = self.client.get('/')
        repo_resp = self.client.get('/%s/' % repo.basename)

        assert(200 == main_resp.status_code)
        assert(404 == repo_resp.status_code)
        assert('Path or File could not be found!' in repo_resp.data)
        assert('%s</a>' % repo.basename not in main_resp.data)

    def test_repo_exists(self):
        repo = self.temp.join('repo1').mkdir()
        self.create_app()

        main_resp = self.client.get('/')
        repo_resp = self.client.get('/%s/' % repo.basename)

        assert(200 == main_resp.status_code)
        assert(200 == repo_resp.status_code)
        assert('%s</a>' % repo.basename in main_resp.data)

    def test_create_path(self):
        main_repo = self.temp.join('repo1')
        sub_repo = main_repo.join('sub_repo1')
        resp = self.client.get('/')

        assert(200 == resp.status_code)
        assert(main_repo.basename not in resp.data)

        resp = self.client.post('/admin/create_folder/',
                                data={'path': '/',
                                      'folder_name': main_repo.basename},
                                follow_redirects=True)

        assert(200 == resp.status_code)
        assert(main_repo.check(dir=True))

        resp = self.client.post('/admin/create_folder/',
                                data={'folder_name': '%s' % sub_repo.basename,
                                      'path': main_repo.basename},
                                follow_redirects=True)

        assert(200 == resp.status_code)
        assert(sub_repo.check(dir=True))

        resp = self.client.get('/%s/' % main_repo.basename)

        assert(200 == resp.status_code)
        assert(sub_repo.basename in resp.data)

    def test_create_path_if_exists(self):
        name = 'repo1'
        name_upper = name.upper()
        main_repo = self.temp.join(name)
        main_repo_upper = self.temp.join(name_upper)
        main_repo.mkdir()
        resp = self.client.get('/')

        assert resp.status_code == 200
        assert main_repo.basename in resp.data
        assert not main_repo_upper.check()

        resp = self.client.post('/admin/create_folder/',
                                data={'folder_name': '%s' %
                                      main_repo.basename.upper()})

        assert resp.status_code == 302
        assert not main_repo_upper.check()
        assert main_repo.basename in resp.headers.get('Location')

    def test_rename_path(self):
        repo = self.temp.join('repo1').mkdir()
        repo_rename = self.temp.join('repo2')

        resp = self.client.get('/')

        assert(200 == resp.status_code)
        assert(repo.basename in resp.data)

        resp = self.client.post('/admin/rename/', data={'current':
                                repo.basename, 'rename': repo_rename.basename},
                                follow_redirects=True)

        assert(200 == resp.status_code)
        assert(not repo.check(dir=True))

        resp = self.client.get('/')

        assert(200 == resp.status_code)
        assert(repo_rename.basename in resp.data)
        assert(repo.basename not in resp.data)

    def test_remove_path(self):
        repo = self.temp.join('repo1').mkdir()
        resp = self.client.get('/')

        assert(200 == resp.status_code)
        assert(repo.basename in resp.data)

        resp = self.client.post('/admin/remove/', data={'item_path':
                                                        repo.basename},
                                follow_redirects=True)

        assert(200 == resp.status_code)
        assert(not repo.check(dir=True))

    def test_upload_file(self):
        repo = self.temp.join('repo').mkdir()
        upload_file = repo.join('uploaded_file.txt')

        assert(not upload_file.check(file=True))

        resp = self.client.post('/admin/upload/',
                                data={'path': repo.basename,
                                      'file': (StringIO('File upload content'),
                                               upload_file.basename)},
                                follow_redirects=True)

        assert(200 == resp.status_code)
        assert(upload_file.check(file=True))

        resp = self.client.get('/%s/' % repo.basename)

        assert(upload_file.basename in resp.data)
