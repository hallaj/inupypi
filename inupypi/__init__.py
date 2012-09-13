#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys, os

from flask import Flask
from flask import abort, render_template, request, send_from_directory
from flask.ext.assets import Environment, Bundle
from unipath import Path
from optparse import OptionParser, OptionValueError

usage = 'Usage: %s [options] [command [command]]' % sys.argv[0]
parser = OptionParser(usage=usage)
parser.add_option('-c', '--config-file', default='config.ini',
        help='Config file, default to config.ini')

(options, args) = parser.parse_args()

app = Flask(__name__)
parent_path = os.path.dirname(app.root_path)
config = app.config.from_pyfile(os.path.join(parent_path, options.config_file))
app.debug = app.config['DEBUG']
app.template_folder = Path(app.root_path, app.template_folder, app.config['TEMPLATE'])

assets = Environment(app)
assets.register('css', Path(app.template_folder, 'static/style.css'),
        output='inupypi.css', filters='cssmin')

package_path = Path(app.config.get('EGGBASKET_REPO'))

if not package_path.isabsolute():
    app.config['EGGBASKET_REPO'] = Path(app.root_path,
            app.config.get('EGGBASKET_REPO'))

import inupypi.views
import inupypi.views.manage
