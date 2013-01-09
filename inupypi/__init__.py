#!/usr/bin/env python
# -*- coding: utf8 -*-

from flask import Flask
from flask.ext.themes import setup_themes
from inupypi.views.admin import admin
from inupypi.views.error import error
from inupypi.views.main import main


def create_app(**config):
    app = Flask(__name__)
    app.config.update(config)
    app.config['THEME'] = app.config.get('THEME', 'inupypi')

    setup_themes(app)

    app.register_blueprint(admin)
    app.register_blueprint(error)
    app.register_blueprint(main)

    return app
