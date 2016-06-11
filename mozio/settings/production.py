__author__ = 'stikks'
from .local import *

import dj_database_url
DATABASES = {'default': dj_database_url.config(engine='django.contrib.gis.db.backends.postgis')}