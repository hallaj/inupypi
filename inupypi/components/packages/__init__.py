#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
from inupypi import abort, app
from pkgtools.pkg import SDist
from unipath import Path


class Package(object):
    filepath = None
    name = None
    author = 'unknown'
    current = None

def get_eggbaskets():
    path = Path(app.config.get('EGGBASKET_REPO', ''))
    if not path.exists() and not path.isdir():
        abort(500, "%s doesn't exist." % path)
    return os.listdir(path)

def get_package_path(eggbasket):
    path = Path(app.config.get('EGGBASKET_REPO', ''), eggbasket)

    if not path.exists() and not path.isdir():
        abort(500)
    return path

def get_packages(eggbasket):
    packages = []
    folders = [Path(folder) for folder in get_package_path(eggbasket).listdir()
            if folder.isdir() and folder.listdir() != []]

    for package in folders:
        p = Package()
        p.filepath = package
        p.current = get_current_package(eggbasket, package)
        p.eggbasket = eggbasket 
        try:
            p.author = SDist(p.current).metadata['PKG-INFO']['Author']
        except Exception:
            pass
        packages.append(p)
    return packages

def get_package_files(eggbasket, package):
    package_path = get_package_path(eggbasket)
    package = package_path.listdir()[[x.name.lower() for x in package_path.listdir()].index(package.lower())]

    package_dir = Path(package_path, package)
    files = []

    for package_file in package_dir.listdir():
        p = Package()
        p.filepath = package_file
        p.eggbasket = eggbasket 
        try:
            p.name = SDist(package_file).name
            p.author = SDist(package_file).metadata['PKG-INFO']['Author']
        except Exception:
            pass
        files.append(p)
    return sorted(files, reverse=True)

def get_current_package(eggbasket, package):
    package_dir = Path(get_package_path(eggbasket), package)
    contents = sorted(package_dir.listdir(), reverse=True)
    return contents[0] if contents else None

def get_metadata(eggbasket, package, filename):
    package_file = Path(get_package_path(eggbasket), package, filename)

    try:
        return SDist(package_file)
    except Exception:
        return None

def get_file(eggbasket, package, filename):
    package_file = Path(get_package_path(eggbasket), package, filename)

    if package_file.exists() and package_file.isfile():
        return package_file
    return False
