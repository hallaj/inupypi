#!/usr/bin/env python
# -*- coding: utf8 -*-

from flask import Flask, Response
from flask import render_template, send_from_directory
from inupypi import settings

app = Flask(__name__)
app.config.from_object(settings)

from inupypi import views
