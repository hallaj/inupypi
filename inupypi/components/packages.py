#!/usr/bin/env python
# -*- coding: utf8 -*-

from inupypi import app
from unipath import Path

def get_packages():
    pkg_path = Path(app.config.get('PKG_PATH'))
    packages = []

    for package in (pkg_path.listdir() if pkg_path.isdir() else []):
        if package.isdir():
            packages.append(package)
    packages.sort()
    return packages

def get_package_files(package):
    pkg_path = Path(app.config.get('PKG_PATH'), package)
    files = []

    for f in (pkg_path.listdir() if pkg_path.isdir() else []):
        files.append(f)
    files.sort(reverse=True)
    return files

def get_file(package, filename):
    package = Path(app.config.get('PKG_PATH', ''), package, filename)

    if package.exists() and package.isfile():
        return package
    return False

def get_latest_file(package):
    packages = get_package_files(package)

    try:
        return Path(packages[0]).name
    except IndexError:
        return False
