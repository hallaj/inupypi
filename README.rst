.. image:: https://travis-ci.org/hallaj/inupypi.png


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

Building the application:

.. code-block :: python

  python setup.py develop



Running the application:

As Standalone WSGI Server

  
.. code-block :: bash

    inupypi_server -H <INSERT HOSTNAME> -p <INSERT PORT> -t <HTPASSWD FILE> <PATH TO REPOSITORY>



Apache mod_wsgi
~~~~~~~~~~~~~~~

1. Create the following file and save it as inupypi.wsgi:

.. code-block :: python

      #!/usr/bin/env python
      # -*- coding: utf8 -*-

      from inupypi import create_app

      config = {'INUPYPI_REPO': '/PATH/TO/REPOSITORY'}
      application = create_app(**config})



2. Add the following Apache configuration to use the wsgi file:


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
2. We wanted to have templates with our pypiserver so that formatting can be easily done.
3. We had a few ideas where we wanted to bring our pypiserver that were not compatible or accepted by current pypiserver implementations.

TODO
----
1. Create automated processes to generate all of the steps above to make the process less manual.

Tests
---------

To run the tests:

.. code-block:: python

  sh
    python setup.py test


