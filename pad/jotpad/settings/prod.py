# prod config goes here!

""" Production specific settings."""
from .base import *

# Parse database configuration from $DATABASE_URL
import dj_database_url


ALLOWED_HOSTS = ['*']

DEBUG = False

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {}

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=False)

# django 4.1
# The line below requires that you update the middleware config by adding
# 'whitenoise.middleware.WhiteNoiseMiddleware',
# to the middleware list in base.py
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# staticfiles
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Ensure STATIC_ROOT exists.
os.makedirs(STATIC_ROOT, exist_ok=True)

# https://docs.djangoproject.com/en/4.1/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

