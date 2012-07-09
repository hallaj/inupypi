#!/usr/bin/env python
# -*- coding: utf8 -*-

from inupypi import abort, app
from unipath import Path


class Package(object):
    package = ''

def get_package_path():
    path = Path(app.config.get('PACKAGE_PATH', ''))

    if not path.exists() and not path.isdir():
        abort(500)
    return path

def get_packages():
    packages = []
    folders = [folder for folder in get_package_path().listdir()
            if folder.isdir()]

    for package in folders:
        packages.append(package.name)
    return packages

def get_package_files(package):
    package_dir = Path(get_package_path(), package)
    files = []

    for package_file in package_dir.listdir():
        files.append(package_file)
    files.sort(reverse=True)
    return files

def get_file(package, filename):
    package_file = Path(get_package_path(), package, filename)

    if package_file.exists() and package_file.isfile():
        return package_file
    return False
