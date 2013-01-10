# inupypi [![Build Status] (https://travis-ci.org/hallaj/inupypi.png)] (https://travis-ci.org/hallaj/inupypi)

#### A Multi Repository PyPI Server Implementation in Python Flask

### Installation Instructions

#### From source:

1. Clone the source code from the Github's repository:
```
  git clone https://github.com/hallaj/inupypi.git
```
2. Create an application file with the following contents. Do substitute the values accordingly:
```python
  #!/usr/bin/env python
  # -*- coding: utf8 -*-

  import inupypi

  config = {'DEBUG': True, 'INUPYPI_REPO': '/PATH/TO/REPOSITORY'}
  app_host = '0.0.0.0'
  app_port = 8080

  app = inupypi.create_app(**config)
  app.run(host=app_host, port=app_port)
```
3. Execute the app.py and you can visit the application at http://REPLACE_WITH_APP_HOST:REPLACE_WITH_APP_PORT/
```sh
  python app.py
  firefox http://127.0.0.1:8080/
```

### Why another pypiserver application ?
1. We could not find another pypiserver that supported multiple eggbaskets.
1. We wanted to have templates with our pypiserver so that formatting can be easily done.
1. We had a few ideas where we wanted to bring our pypiserver that were not compatible or accepted by current pypiserver implementations.

### TODO
1. Create automated processes to generate all of the steps above to make the process less manual

### Tests
  To run the tests
```sh
  python setup.py develop
  python setup.py test
```
