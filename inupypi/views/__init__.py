#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

from inupypi import app, render_template, send_from_directory
from inupypi import Response
from inupypi.components.packages import Packages, PackageInfo
from inupypi.settings import PACKAGE_PATH


@app.route('/')
def index():
    return render_template('index.html', packages=Packages().get_folders())


@app.route('/<pkg>/')
def fetch_package(pkg):
    return package(pkg)


@app.route('/package/<package>/')
def package(package):
    return render_template('packages.html', name=package,
            packages=Packages().get_packages(package))


@app.route('/package/<package>/get/<filename>')
def package_get(package, filename):
    return send_from_directory(os.path.join(PACKAGE_PATH, package), filename,
            as_attachment=True)


@app.route('/package/<package>/metadata/<filename>')
def package_metadata(package, filename):
    package_info = PackageInfo(package_path=os.path.join(PACKAGE_PATH,
        package), filename=filename).pkg_info
    return render_template('metadata.html', info=package_info,
            filename=filename)
