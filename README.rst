=======
inupypi
=======

inetutils PyPI Server Project

To run in command line:

1. To install::

    pip install inupypi

2. create config.ini with the following content::

    DEBUG = True
    INUPYPI_REPO = '<FULL PATH TO EGG BASKETS PARENT DIRECTORY>'

3. run app.py::

    python app.py

To run inupypi under apache mod_wsgi:

1. Install inupypi::

    pip install inupypi

2. create config.ini with the following content (This will not be necessary once configure distcmd is done)::

    DEBUG = False
    INUPYPI_REPO = '<FULL PATH TO INUPYPI REPO>'

3. edit and then save the httpd-inupypi.conf.sample into httpd's conf directory and ensure it's being included in httpd.conf

4. start / restart your apache and browse to http://httpd_host/inupypi

Why another pypiserver application ?
====================================

1. We could not find another pypiserver that supported multiple eggbaskets.

2. We wanted to have templates with our pypiserver so that formatting can be easily done.

3. We had a few ideas where we wanted to bring our pypiserver that were not compatible or accepted by current pypiserver implementations.

TODO
====

1. Create automated processes to generate all of the steps above to make the process less manual


Tests
=====

To run the tests::

    1. python setup.py develop

    2. export export INUPYPI_SETTINGS=<full path to config.ini>

    3. python setup.py test
