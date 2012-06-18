#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

from inupypi.settings import PACKAGE_PATH
from pkgtools.pkg import get_metadata


class PackageInfo(object):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.local_version = kwargs.get('version')
        self.release_version = ''
        self.filename = kwargs.get('filename')
        self.size = kwargs.get('size')

        if kwargs.get('package_path'):
            self.pkg_info = get_metadata(str(os.path.join(
                kwargs.get('package_path'), kwargs.get('filename')))).pkg_info


class Packages(object):
    def get_folders(self):
        folders = []

        for package in os.listdir(PACKAGE_PATH):
            if os.path.isdir(os.path.join(PACKAGE_PATH, package)):
                folders.append(PackageInfo(name=package,
                    version=self.get_latest(package)))
        return folders

    def get_latest(self, package):
        package_contents = os.listdir(os.path.join(PACKAGE_PATH, package))
        package_contents.sort()

        try:
            return package_contents[-1:][0]
        except IndexError:
            return False

    def get_packages(self, package):
        packages = []

        files = os.listdir(os.path.join(PACKAGE_PATH, package))
        files.sort(reverse=True)

        for f in files:
            packages.append(PackageInfo(name=package, filename=f,
                package_path=os.path.join(PACKAGE_PATH, package)))
        return packages
