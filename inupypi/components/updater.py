#!/usr/bin/env python
# -*- coding: utf8 -*-

from inupypi.settings import REMOTE_PYPI
from xmlrpclib import Server

class Updater(object):
    def __init__(self):
        self.pypi = Server(REMOTE_PYPI)

    def get_releases(self, package_name):
        return self.pypi.package_releases(package_name)[0]
