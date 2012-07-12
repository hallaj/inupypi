#!/usr/bin/env python
# -*- coding: utf8 -*-

from inupypi import abort, app
from pkgtools.pkg import SDist
from unipath import Path


class Package(object):
    filepath = None
    description = None
    current = None

def get_package_path():
    path = Path(app.config.get('PACKAGE_PATH', ''))

    if not path.exists() and not path.isdir():
        abort(500)
    return path

def get_packages():
    packages = []
    folders = [Path(folder) for folder in get_package_path().listdir()
            if folder.isdir() and folder.listdir() != []]

    for package in folders:
        p = Package()
        p.filepath = package
        p.current = get_current_package(package)
        try:
            p.description = SDist(p.current)
        except Exception:
            pass
        packages.append(p)
    return packages

def get_package_files(package):
    package_dir = Path(get_package_path(), package)
    files = []

    for package_file in package_dir.listdir():
        p = Package()
        p.filepath = package_file
        try:
            p.description = SDist(package_file)
        except Exception:
            pass
        files.append(p)
    return sorted(files, reverse=True)

def get_current_package(package):
    package_dir = Path(get_package_path(), package)
    contents = sorted(package_dir.listdir(), reverse=True)
    return contents[0] if contents else None

def get_metadata(package, filename):
    package_file = Path(get_package_path(), package, filename)

    try:
        return SDist(package_file)
    except Exception:
        return None

def get_file(package, filename):
    package_file = Path(get_package_path(), package, filename)

    if package_file.exists() and package_file.isfile():
        return package_file
    return False
