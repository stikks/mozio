__author__ = 'stikks'
from .local import *

import dj_database_url
POSTGRES_URL = "postgres://hykhvgqncmpxqa:FVHYS7iCEiJ565wfM-QPVLPkNo@ec2-54-235-65-139.compute-1.amazonaws.com:5432/d1f475em3up1gj"
DATABASES = {'default': dj_database_url.config(default=os.environ[POSTGRES_URL])}