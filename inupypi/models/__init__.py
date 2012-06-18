#!/usr/bin/env python
# -*- coding: utf8 -*-

from inupypi import app
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
