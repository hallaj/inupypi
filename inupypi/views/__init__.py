#!/usr/bin/env python
# -*- coding: utf8 -*-

from flask import current_app as app
from flask.ext.themes import render_theme_template


def render(template, **kwargs):
    return render_theme_template(app.config.get('THEME'), template, **kwargs)
