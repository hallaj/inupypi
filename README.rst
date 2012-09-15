=======
inupypi
=======

inetutils PyPI Server Project

To run in command line:

1. To install::

    pip install inupypi

2. create config.ini with the following content::

    DEBUG = True
    EGGBASKET_REPO = '<FULL PATH TO EGG BASKETS PARENT DIRECTORY>'

3. run app.py::

    python app.py

To run inupypi under apache mod_wsgi:

1. Install inupypi::

    pip install inupypi

2. Edit the supplied app.py commenting out the last line leaving only::

    import os
    os.environ["INUPYPI_SETTINGS"] = os.path.dirname(os.path.realpath(__file__)) + '/config.ini'
    from inupypi import app as application

3. create config.ini with the following content (This will not be necessary once configure distcmd is done)::

    DEBUG = False
    EGGBASKET_REPO = '<FULL PATH TO EGG BASKETS PARENT DIRECTORY>'

4. create apache conf file with the following content and save it on /etc/apache/conf.d/inupypi::

        WSGIScriptAlias /inupypi  <FULL PATH OF YOUR app.py created on step 2>
        WSGIDaemonProcess inupypi user=<USER> group=<GROUP>\
            home=<FULL PATH OF app.py parent directory> \
            python-path=<PYTHON PATH>

        <Location /inupypi>
            WSGIProcessGroup inupypi
            WSGIPassAuthorization On
        </Location>

TODO
====

1. Create automated processes to generate all of the steps above to make the process less manual

Tests
=====

To run the tests::

    1. export INUPYPI_SETTINGS = "<FULL PATH OF CONFIG FILE>"

    2. python setup.py test
