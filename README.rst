# inupypi [![Build Status] (https://travis-ci.org/hallaj/inupypi.png)] (https://travis-ci.org/hallaj/inupypi)

#### A Multi Repository PyPI Server Implementation in Python Flask

### Installation Instructions

#### From source:

1. Clone the source code from the Github's repository:
```
  git clone https://github.com/hallaj/inupypi.git
```

1. Building the application:
```
  python setup.py develop
```

1. Running the application:

  ##### Standalone WSGI Server:
  ```
    inupypi_server -H <INSERT HOSTNAME> -p <INSERT PORT> -t <HTPASSWD FILE> <PATH TO REPOSITORY>
  ```

  ##### Apache mod_wsgi:

    1. Create the following file and save it as inupypi.wsgi:
    ```
      #!/usr/bin/env python
      # -*- coding: utf8 -*-

      from inupypi import create_app

      config = {'INUPYPI_REPO': '/PATH/TO/REPOSITORY'}
      application = create_app(**config})
    ```
    1. Add the following Apache configuration to use the wsgi file:
    ```
      <VirtualHost *:80>
          ServerName      SERVER_NAME

          WSGIScriptAlias / /PATH/TO/inupypi.wsgi
          WSGIDaemonProcess inupypi user=APACHE_USER group=APACHE_GROUP home=/PATH/TO/INUPYPI python-path=/PATH/TO/PYTHON/SITE-PACKAGES/WHERE/INUPYPI/IS/INSTALLED

          <Location />
              WSGIProcessGroup inupypi
              WSGIPassAuthorization On
          </Location>
      </VirtualHost>
    ```

### Why another pypiserver application ?
1. We could not find another pypiserver that supported multiple repositories.
1. We wanted to have templates with our pypiserver so that formatting can be easily done.
1. We had a few ideas where we wanted to bring our pypiserver that were not compatible or accepted by current pypiserver implementations.

### TODO
1. Create automated processes to generate all of the steps above to make the process less manual.

### Tests
1. To run the tests:

```sh
  python setup.py test
```
