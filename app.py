import os
os.environ["INUPYPI_SETTINGS"] = os.path.dirname(os.path.realpath(__file__)) + '/config.ini'
from inupypi import app as application
application.run()
