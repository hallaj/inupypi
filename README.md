inupypi
=======

inetutils PyPI Server Project

To run in command line:

    1. pip install inupypi
    
    2. create app.py with the following content:
    
        import os
        os.environ["INUPYPI_SETTINGS"] = os.path.dirname(os.path.realpath(__file__)) + '/config.ini'
        from inupypi import app as application
        application.run()
    
    3. create config.ini with the following content:
    
        DEBUG = True 
        EGGBASKET_REPO = '<FULL PATH TO EGG BASKETS PARENT DIRECTORY>'
    
    4. run app.py 
    
        python app.py

To run under apache mod_wsgi:

    1. pip install inupypi
    
    2. create app.py with the following content:
    
        import os
        os.environ["INUPYPI_SETTINGS"] = os.path.dirname(os.path.realpath(__file__)) + '/config.ini'
        from inupypi import app as application

    3. create config.ini with the following content:
    
        DEBUG = False 
        EGGBASKET_REPO = '<FULL PATH TO EGG BASKETS PARENT DIRECTORY>'

    4. create apache conf file with the following content and save it on /etc/apache/conf.d/inupypi
    
        WSGIScriptAlias /inupypi  <FULL PATH OF YOUR app.py created on step 2>
        WSGIDaemonProcess inupypi user=<USER> group=<GROUP>\
            home=<FULL PATH OF app.py parent directory> \
            python-path=<PYTHON PATH>

        <Location /inupypi>
            WSGIProcessGroup inupypi
            WSGIPassAuthorization On
        </Location>

tests
=====

To run the tests: 

    1. export INUPYPI_SETTINGS = "<FULL PATH OF CONFIG FILE>"

    2. python setup.py test
