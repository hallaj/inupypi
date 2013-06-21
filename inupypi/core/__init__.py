#!/usr/bin/env python
# -*- coding: utf8 -*-

from flask import abort, current_app
from inupypi.core.exceptions import InuPyPI404Exception, InuPyPIMissingRepoPath
from pkg_resources import parse_version
from unipath import Path


class Dirs(object):
    def __init__(self, path):
        self.__parents__ = None
        self.__contents__ = None

        try:
            path = Path(path)

            self.__parents__ = path
            self.__contents__ = sorted([dir_.absolute() for dir_ in
                                        path.listdir()
                                        if dir_.isdir() or dir_.isfile()],
                                       key=lambda v: parse_version(v))
        except:
            pass


def content(request=None):
    base = Path(current_app.config.get('INUPYPI_REPO',
                Path('.', 'packages')))

    if request:
        repo = Path(base, request)
    else:
        repo = base

    try:
        repo = repo.absolute()
        base = base.absolute()

        if not repo.exists():
            if base == repo:
                raise InuPyPIMissingRepoPath

            # sets the request to lowercase and compares it with
            # the existing items in the repository in lowercase
            repo = search_path(repo, base)

            if not repo:
                raise InuPyPI404Exception

        if repo.isdir():
            return Dirs(repo)
        if repo.isfile():
            return repo

    except InuPyPIMissingRepoPath:
        abort(500, 'Missing repository or package path!')
    except InuPyPI404Exception:
        abort(404, 'Path or File could not be found!')
    except:
        abort(500, 'Internal Server Error!')
    return repo


def sanitize_path(path):
    return path if not path.startswith('/') else path[1:]


def search_path(path, repo):
    try:
        repo = Path(repo).absolute()
        walk = list(repo.walk())

        for item in walk:
            if item.lower() == Path(repo, path).lower():
                return item
    except:
        pass
    return False
