__author__ = 'stikks'
from .local import *

import dj_database_url
POSTGRES_URL = "HEROKU_POSTGRESQL_<DB_NAME>_URL"
DATABASES = {'default': dj_database_url.config(default=os.environ[POSTGRES_URL])}