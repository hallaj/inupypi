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
    return render_template('index.html', eggbaskets=get_eggbaskets())

@app.route('/<eggbasket>/')
def eggbasket(eggbasket):
    return render_template('eggbasket.html', packages=get_packages(eggbasket))


@app.route('/<eggbasket>/<package_name>/')
def package(eggbasket, package_name):
    return render_template('package.html',
            files=get_package_files(eggbasket, package_name))


@app.route('/package/metadata/<eggbasket>/<package>/<filename>/')
def package_metadata(eggbasket, package, filename):
    return render_template('metadata.html',
            metadata=get_metadata(eggbasket, package, filename))


@app.route('/<eggbasket>/<package_name>/get/<filename>')
def package_get(eggbasket, package_name, filename):
    package = get_file(eggbasket, package_name, filename)

    
    if package:
        return send_from_directory(package.parent, package.name,
                as_attachment=True)
    abort(404)
