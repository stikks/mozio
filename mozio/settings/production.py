__author__ = 'stikks'

from .base import *
import dj_database_url

DATABASES = {
    'default': dj_database_url.config()
}

ALLOWED_HOSTS = ['*']

DEBUG = False

SECRET_KEY = 'y523x-9_!*n)jj!s@r@k1%j=59p64&5pnqfxx=f073&dgc6d7e'