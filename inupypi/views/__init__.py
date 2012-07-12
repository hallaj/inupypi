#!/usr/bin/env python
# -*- coding: utf8 -*-

from inupypi import abort, app, render_template, send_from_directory
from inupypi.components.packages import *


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500


@app.route('/')
def index():
    return render_template('index.html', packages=get_packages())


@app.route('/<package_name>/')
def package(package_name):
    return render_template('package.html',
            files=get_package_files(package_name))


@app.route('/package/metadata/<package>/<filename>/')
def package_metadata(package, filename):
    return render_template('metadata.html',
            metadata=get_metadata(package, filename))


@app.route('/<package_name>/get/<filename>')
def package_get(package_name, filename):
    package = get_file(package_name, filename)

    if package:
        return send_from_directory(package.parent, package.name,
                as_attachment=True)
    abort(404)
