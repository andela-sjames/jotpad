# prod config goes here!

""" Production specific settings."""
from .base import *

ALLOWED_HOSTS = ['*']

DEBUG = False

SITE_ID = 1

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# staticfiles
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Ensure STATIC_ROOT exists.
os.makedirs(STATIC_ROOT, exist_ok=True)

# https://docs.djangoproject.com/en/4.1/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

