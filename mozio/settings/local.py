__author__ = 'stikks'

from .base import *

DATABASES = {
  'default': {
      'ENGINE': 'django.contrib.gis.db.backends.postgis',
      'NAME': "mozio",
      'USERNAME': 'postgres',
      'PASSWORD': 'postgres',
      'HOST': '',
      'PORT': ''
  }
}