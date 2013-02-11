#!/usr/bin/env python
# -*- coding: utf8 -*-

from flask import Blueprint, abort, current_app, redirect, request, url_for
from flask.ext import htauth
from inupypi.core import sanitize_path, search_path
from unipath import Path
from werkzeug import secure_filename

admin = Blueprint('admin', __name__)


@admin.route('/admin/create_folder/', methods=['POST'])
@htauth.authenticated
def create_folder():
    base = Path(current_app.config.get('INUPYPI_REPO',
                Path('.', 'packages')))
    path = sanitize_path(request.form.get('path', ''))
    folder = sanitize_path(request.form.get('folder_name', ''))

    if Path(path, folder):
        temp_base = Path(base, path).absolute()
        create_path = Path(temp_base, folder)

        if create_path.exists():
            return redirect('%s' % Path(path, folder))
        search = search_path(folder, temp_base)

        if search:
            base = Path(base).absolute()
            return redirect('%s' % sanitize_path(search.replace(base, '')))

        try:
            create_path.mkdir(parents=True)
        except Exception, e:
            status = 'Failed to create %s' % e
            abort(500, status)
    if request.referrer:
        return redirect(request.referrer)
    return redirect(url_for('main.index'))


@admin.route('/admin/rename/', methods=['POST'])
@htauth.authenticated
def rename():
    base = Path(current_app.config.get('INUPYPI_REPO',
                Path('.', 'packages')))
    current = request.form.get('current')
    rename = request.form.get('rename')

    if current and rename:
        try:
            Path(base, current).rename(Path(base, rename))
        except Exception, e:
            status = 'Failed to rename %s' % e
            abort(500, status)
    if request.referrer:
        return redirect(request.referrer)
    return redirect(url_for('main.index'))


@admin.route('/admin/remove/', methods=['POST'])
@htauth.authenticated
def remove():
    base = Path(current_app.config.get('INUPYPI_REPO',
                Path('.', 'packages')))
    path = sanitize_path(request.form.get('item_path'))

    if path:
        try:
            Path(base, path).rmtree()
        except Exception, e:
            status = 'Failed to remove %s' % e
            abort(500, status)
    if request.referrer:
        return redirect(request.referrer)
    return redirect(url_for('main.index'))


@admin.route('/admin/upload/', methods=['POST'])
@htauth.authenticated
def upload():
    base = Path(current_app.config.get('INUPYPI_REPO',
                Path('.', 'packages')))
    path = request.form.get('path')
    upload_file = request.files.get('file')

    if upload_file and path:
        path = sanitize_path(path)

        try:
            filename = secure_filename(upload_file.filename)
            upload_file.save(Path(base, path, filename))
        except Exception, e:
            status = 'Failed to upload %s to %s: %s' % (upload_file.filename,
                                                        path, e)
            abort(500, status)
    if request.referrer:
        return redirect(request.referrer)
    return redirect(url_for('main.index'))
