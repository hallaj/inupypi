#!/usr/bin/env python
# -*- coding: utf8 -*-

from flask import Flask, Response
from flask import abort, render_template, send_from_directory
from flask.ext.assets import Environment, Bundle
from inupypi import config
from unipath import Path

app = Flask(__name__)
app.config.from_object(config)
app.template_folder = Path(app.root_path, app.template_folder, config.TEMPLATE)

assets = Environment(app)
assets.register('css', Path(app.template_folder, 'static/style.css'),
        output='inupypi.css', filters='cssmin')

pkg_path = Path(app.config.get('PKG_PATH', ''))

if not pkg_path.isabsolute():
    app.config['PKG_PATH'] = Path(app.root_path, pkg_path)

import inupypi.views
