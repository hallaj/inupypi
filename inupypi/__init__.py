#!/usr/bin/env python
# -*- coding: utf8 -*-

from argparse import ArgumentParser
from flask import Flask
from flask.ext import htauth
from flask.ext.themes import setup_themes
from inupypi.views.admin import admin
from inupypi.views.error import error
from inupypi.views.main import main
from unipath import Path


def create_app(**config):
    app = Flask(__name__)
    app.config['HTAUTH_HTPASSWD_PATH'] = Path(__file__, '..',
                                              'htpasswd').absolute()
    app.config['HTAUTH_REALM'] = 'inupypi Authentication'
    app.config['THEME'] = app.config.get('THEME', 'inupypi')

    setup_themes(app)
    htauth.HTAuth(app)

    app.config.update(config)
    app.register_blueprint(admin)
    app.register_blueprint(error)
    app.register_blueprint(main)

    return app


def app():
    parser = ArgumentParser(description='inupypi Standalone Server')
    parser.add_argument('-d', '--DEBUG', action='store_true', default=False,
                        help='enable debug mode')
    parser.add_argument('-H', '--HOST', default='127.0.0.1',
                        help='Server Listen address')
    parser.add_argument('-p', '--PORT', default='8080',
                        help='Server Listen port')
    parser.add_argument('-t', '--HTAUTH_HTPASSWD_PATH',
                        default=Path(__file__, '..', 'htpasswd').absolute(),
                        help='htpasswd file for authentication.')
    parser.add_argument('INUPYPI_REPO', help='path to repository')
    args = vars(parser.parse_args())
    app = create_app(**args)
    app.run(host=args.get('HOST'), port=int(args.get('PORT')))


if __name__ == '__main__':
    app()
