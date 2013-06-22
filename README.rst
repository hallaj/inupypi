.. -*- mode: rst; coding: utf-8 -*-

===============================================================================================
A Multi Repository PyPI Server Implemented in Python Flask
===============================================================================================

.. image:: https://travis-ci.org/hallaj/inupypi.png



Installation Instructions
-------------------------

From source
~~~~~~~~~~~

Clone the source code from the Github's repository::



  git clone https://github.com/hallaj/inupypi.git



Building the application::


  python setup.py develop



Running the application
-----------------------

Inupypi can be run using the usual apache mod_wsgi setup as well as stand alone mode.

As Standalone WSGI Server::


    inupypi_server -H <INSERT HOSTNAME> -p <INSERT PORT> -t <HTPASSWD FILE> <PATH TO REPOSITORY>



Apache mod_wsgi
~~~~~~~~~~~~~~~

1. To run using apache mod_wsgi, create the following file and save it as inupypi.wsgi::


      #!/usr/bin/env python
      # -*- coding: utf8 -*-

      from inupypi import create_app

      config = {'INUPYPI_REPO': '/PATH/TO/REPOSITORY'}
      application = create_app(**config})



2. Add the following Apache configuration to use the above defined wsgi file::


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

To run the tests::


  sh
    python setup.py test


