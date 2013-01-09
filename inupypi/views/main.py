#!/usr/bin/env python
# -*- coding: utf8 -*-

from flask import Blueprint, send_from_directory
from inupypi.core import content
from inupypi.views import render
from unipath import Path

main = Blueprint('main', __name__)


@main.route('/', defaults={'route': None})
@main.route('/<path:route>/')
def index(route):
    contents = content(route)

    if isinstance(contents, Path) and contents.isfile():
        return send_from_directory(contents.parent, str(contents.name),
                                   as_attachment=True)
    return render('index.html', contents=contents)


@main.route('/about/')
def about():
    return render('about.html')
