#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, send_from_directory
from inupypi.core import content
from inupypi.views import render
from unipath import Path
from inupypi.core.bread import Bread

main = Blueprint('main', __name__)


@main.route('/', defaults={'route': None})
@main.route('/<path:route>/')
def index(route):
    contents = content(route)
    if route:
        bread_route = route
    else:
        bread_route = ''
    bread = Bread(url_for('main.index',
                          _external=True) + bread_route)
    if isinstance(contents, Path) and contents.isfile():
        return send_from_directory(contents.parent, str(contents.name),
                                   as_attachment=True)
    return render('index.html', bread=bread, contents=contents)


@main.route('/about/')
def about():
    return render('about.html')
