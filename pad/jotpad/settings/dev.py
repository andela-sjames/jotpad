from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SQLITE = False

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


if SQLITE is True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('POSTGRES_DB'),
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'HOST': os.environ.get('POSTGRESDB_HOST'),
            'PORT': os.environ.get('POSTGRESDB_PORT'),
            'TEST': {
                'CHARSET': None,
                'COLLATION': None,
                'NAME': os.path.join(os.path.dirname(__file__), 'test.db'),
                'MIRROR': None
            }
        }
    }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
