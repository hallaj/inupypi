#!/usr/bin/env python
# -*- coding: utf8 -*-

from inupypi import abort, app, render_template, send_from_directory
from inupypi.components.packages import *
from flask import request, redirect, url_for


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error), 500

@app.route('/')
def index():
    return render_template('index.html', eggbaskets=get_eggbaskets())

@app.route('/<eggbasket>/')
def eggbasket(eggbasket):
    return render_template('eggbasket.html', eggbasket=eggbasket, packages=get_packages(eggbasket))


@app.route('/<eggbasket>/<package_name>/')
def package(eggbasket, package_name):
    return render_template('package.html',
            files=get_package_files(eggbasket, package_name), eggbasket=eggbasket, package=package_name)


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

@app.route('/createeggbasket', methods=['POST'])
def createeggbasket():
    if request.form['eggbasket'].isalpha():
        create_eggbasket(request.form['eggbasket'])
    return redirect(url_for('index'))

@app.route('/createpackagefolder', methods=['POST'])
def createpackagefolder():
    if request.form['package'].isalpha():
        create_package_folder(request.form['eggbasket'], request.form['package'])
    return redirect(url_for('eggbasket', eggbasket=request.form['eggbasket']))

@app.route('/uploadfile', methods=['POST'])
def uploadfile():
    upload_file(request.form['eggbasket'], request.form['package'], request.files['eggfile'])
    return redirect(url_for('package', eggbasket=request.form['eggbasket'], package_name=request.form['package']))
