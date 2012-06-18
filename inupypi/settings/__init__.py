#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

# APPLICATION STATIC DIR
HERE = os.path.realpath(os.path.dirname(__file__))
PACKAGE_PATH = os.path.realpath(os.path.join(HERE, '..', 'packages'))
DATABASE_PATH = os.path.realpath(os.path.join(HERE, '..', 'db'))

# REMOTE PYPI SERVER
REMOTE_PYPI = 'http://pypi.python.org/pypi/'

# Flask
DEBUG = True

# SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'sqlite://%s/db.sqlite' % DATABASE_PATH
SQLALCHEMY_ECHO = DEBUG
