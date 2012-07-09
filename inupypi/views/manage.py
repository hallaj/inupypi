#!/usr/bin/env python
# -*- coding: utf8 -*-

import tempfile

from inupypi import app, render_template, request
from inupypi.components.packages.manage import upload_package
from unipath import Path
from werkzeug import secure_filename


@app.route('/inupypi/manage/')
def manage():
    return render_template('manage/index.html')


@app.route('/inupypi/manage/package/add/', methods=['GET', 'POST'])
def package_add():
    if request.method == 'POST':
        uploaded_file = request.files['package']

        if uploaded_file:
            upload_package(uploaded_file)
    return render_template('manage/add_package.html')


@app.route('/inupypi/manage/package/remove/')
def package_del():
    return render_template('manage/remove_package.html')


@app.route('/inupypi/manage/package/update/')
def package_update():
    return render_template('manage/update_package.html')
