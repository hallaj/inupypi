.. image:: https://travis-ci.org/hallaj/inupypi.png 
.. image:: https://coveralls.io/repos/hallaj/inupypi/badge.png?branch=master :target: https://coveralls.io/r/hallaj/inupypi?branch=master 


A Multi Repository PyPI Server Implementation in Python Flask
=============================================================

Installation Instructions
-------------------------

From source
~~~~~~~~~~~

Clone the source code from the Github's repository:

::

  git clone https://github.com/hallaj/inupypi.git

::

Building the application


.. code-block :: python

  python setup.py develop



Running the application
-----------------------

Inupypi can be run using the usual apache mod_wsgi setup as well as stand alone mode.

As Standalone WSGI Server


.. code-block :: bash

    python inupypi -H <INSERT HOSTNAME> -p <INSERT PORT> -t <HTPASSWD FILE> <PATH TO REPOSITORY>



Apache mod_wsgi
~~~~~~~~~~~~~~~

1. To run using apache mod_wsgi, create the following file and save it as inupypi.wsgi:

.. code-block :: python

      #!/usr/bin/env python
      # -*- coding: utf8 -*-

      from inupypi.__main__ import create_app

      config = {'INUPYPI_REPO': '/PATH/TO/REPOSITORY'}
      application = create_app(**config})



2. Add the following Apache configuration to use the above defined wsgi file:


.. code-block:: bash

      <VirtualHost *:80>
          ServerName      SERVER_NAME

          WSGIScriptAlias / /PATH/TO/inupypi.wsgi
          WSGIDaemonProcess inupypi user=APACHE_USER group=APACHE_GROUP home=/PATH/TO/INUPYPI python-path=/PATH/TO/PYTHON/SITE-PACKAGES/WHERE/INUPYPI/IS/INSTALLED

          <Location />
              WSGIProcessGroup inupypi
              WSGIPassAuthorization On
          </Location>
      </VirtualHost>




FAQ: Why another pypiserver application ?
-----------------------------------------

1. We could not find another pypiserver that supported multiple repositories.

#. We wanted to have templates with our pypi server so that formatting can be easily done.

#. We had a few ideas where we wanted to bring our pypi server that were not compatible or accepted by one of the pypi server implementations.

TODO
----
1. Create automated processes to generate all of the steps above to make the process less manual.
#. Auto resolving and updating of package versions.

Tests
---------

To run the tests:

.. code-block:: python

  sh
    python setup.py test




.. image:: https://d2weczhvl823v0.cloudfront.net/hallaj/inupypi/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

