#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import re

from inupypi import abort, app
from pkg_resources import parse_version
from pkgtools.pkg import SDist
from unipath import Path
from werkzeug import secure_filename


def better_sorted(items, reverse=False):
    convert = lambda text: ('', int(text)) if text.isdigit() else (text, 0)
    alphanum = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(items, key=alphanum, reverse=reverse)


class Package(object):
    filepath = None
    name = None
    author = None
    current = None

    def __lt__(self, other):
        return parse_version(self.name) > parse_version(other.name)


def get_eggbaskets():
    path = Path(app.config.get('INUPYPI_REPO', ''))
    if not path.exists() and not path.isdir():
        abort(500, "%s doesn't exist." % path)
    return os.listdir(path)


def get_package_path(eggbasket):
    path = Path(app.config.get('INUPYPI_REPO', ''), eggbasket)

    if not path.exists() and not path.isdir():
        abort(500)
    return path


def get_packages(eggbasket):
    packages = []
    folders = [Path(folder) for folder in get_package_path(eggbasket).listdir()
               if folder.isdir()]

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
    package = package_path.listdir()[[x.name.lower()
                                     for x in package_path.listdir()
                                      ].index(package.lower())]

    package_dir = Path(package_path, package)
    files = []

    for package_file in package_dir.listdir():
        p = Package()
        p.filepath = package_file
        p.eggbasket = eggbasket
        p.name = p.filepath.name
        p.author = None
        files.append(p)
    return sorted(files)


def get_current_package(eggbasket, package):
    package_dir = Path(get_package_path(eggbasket), package)
    contents = better_sorted(package_dir.listdir(), reverse=True)
    return contents[0] if contents else 'unknown'


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


def create_eggbasket(eggbasket):
    os.makedirs(Path(app.config.get('INUPYPI_REPO'), eggbasket))


def create_package_folder(eggbasket, package):
    os.makedirs(Path(app.config.get('INUPYPI_REPO'), eggbasket, package))


def upload_file(eggbasket, package, f):
    filename = secure_filename(f.filename)
    f.save(Path(app.config.get('INUPYPI_REPO'), eggbasket, package, filename))
