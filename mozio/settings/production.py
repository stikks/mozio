__author__ = 'stikks'

import dj_database_url
from .base import *

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
# DATABASES = dict()
#
# DATABASES['default'] = dj_database_url.config()
# DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

ALLOWED_HOSTS = ['*']