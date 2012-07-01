#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

from inupypi import abort, app, render_template, send_from_directory
from inupypi.components.packages import get_file, get_latest_file, \
        get_packages, get_package_files


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def index():
    return render_template('index.html', packages=get_packages())


@app.route('/<name>/')
def fetch_package(name):
    return package(name)


@app.route('/package/<name>/')
def package(name):
    return render_template('package.html', files=get_package_files(name))


@app.route('/package/<name>/get/<filename>')
def get_package(name, filename):
    package = get_file(name, filename)

    if package:
        return send_from_directory(package.parent, package.name,
                as_attachment=True)
    abort(404)
