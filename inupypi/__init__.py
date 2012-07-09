#!/usr/bin/env python
# -*- coding: utf8 -*-

from flask import Flask
from flask import abort, render_template, request, send_from_directory
from flask.ext.assets import Environment, Bundle
from inupypi import config
from unipath import Path

app = Flask(__name__)
app.config.from_object(config)
app.template_folder = Path(app.root_path, app.template_folder, config.TEMPLATE)

assets = Environment(app)
assets.register('css', Path(app.template_folder, 'static/style.css'),
        output='inupypi.css', filters='cssmin')

package_path = Path(app.config.get('PACKAGE_PATH'))

if not package_path.isabsolute():
    app.config['PACKAGE_PATH'] = Path(app.root_path,
            app.config.get('PACKAGE_PATH'))

import inupypi.views
import inupypi.views.manage
