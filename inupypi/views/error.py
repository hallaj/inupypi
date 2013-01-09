#!/usr/bin/env python
# -*- coding: utf8 -*-

from flask import Blueprint
from inupypi.views import render

error = Blueprint('errors', __name__)


@error.app_errorhandler(403)
def forbidden(err):
    return render('403.html', error=err), 403


@error.app_errorhandler(404)
def page_not_found(err):
    return render('404.html', error=err), 404


@error.app_errorhandler(500)
def internal_server_error(err):
    return render('500.html', error=err), 500
