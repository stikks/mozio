__author__ = 'stikks'

from .base import *
import dj_database_url

DATABASES = {
    'default': dj_database_url.config()
}

ALLOWED_HOSTS = ['*']

DEBUG = False