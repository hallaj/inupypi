#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import tarfile

from unipath import Path

def env_create_packages(workspace, packages, files=False):
    for p in packages:
        if not files:
            Path(workspace, 'test', p).mkdir(parents=True)
        else:
            Path(workspace, 'test', p).write_file('')

def env_create_package_files(workspace, packages, files):
    for p in packages:
        if files:
            for f in files:
                f = Path(workspace, 'test', p, f)
                f.mkdir(parents=True)
                version = '.'.join([x for x in f.name if x.isdigit()])
                i = env_create_package_pkginfo(p, version)
                Path(f, '%s.egg-info' % f.name).mkdir()
                Path(f, 'PKG-INFO').write_file(i)
                Path(f, '%s.egg-info' % f.name, 'PKG-INFO').write_file(i)

                os.chdir(f.parent)
                tar = tarfile.open('%s.tar.gz' % f, 'w:gz')
                tar.add('%s' % f.name)
                tar.close()
                f.rmtree()
        else:
            Path(workspace, 'test', p).mkdir(parents=True)

def env_create_package_pkginfo(name, version):
    c = []
    c.append('Metadata-Version: 1.0')
    c.append('Name: %s' % name)
    c.append('Version: %s' % version)
    c.append('Summary: ')
    c.append('Home-page: ')
    c.append('Author: ')
    c.append('Author-email: ')
    c.append('License: ')
    c.append('Description: ')
    c.append('Platform: ')
    c.append('Classifier:')

    i = '\r\n'.join(c)
    i = '%s\r\n' % i

    return i
