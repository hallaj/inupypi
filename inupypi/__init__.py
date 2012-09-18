#!/usr/bin/env python
# -*- coding: utf8 -*-

from flask import Flask
from flask import abort, render_template, request, send_from_directory
from flask.ext.assets import Environment
from unipath import Path

app = Flask(__name__)
app.template_folder = Path(Path(__file__).parent, 'templates/default')

assets = Environment(app)
assets.register('css', Path(app.template_folder, 'static/style.css'),
        output='inupypi.css', filters='cssmin')

import inupypi.views
