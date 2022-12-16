"""Define Application wide logging here.
"""

LOGGING = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'verbose': {
                    'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                               'pathname=%(pathname)s lineno=%(lineno)s ' +
                               'funcname=%(funcName)s %(message)s'),
                    'datefmt': '%Y-%m-%d %H:%M:%S'
                },
                'simple': {
                    'format': '%(asctime)s %(module)-8s %(levelname)-8s %(name)-15s %(message)s',
                },
            },
            'filters': {
                'require_debug_true': {
                    '()': 'django.utils.log.RequireDebugTrue',
                },
                'require_debug_false': {
                    '()': 'django.utils.log.RequireDebugFalse',
                },
            },
            'handlers': {
                'null': {
                    'level': 'DEBUG',
                    'class': 'logging.NullHandler',
                },
                'console': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'verbose'
                },
                'mail_admins': {
                    'level': 'ERROR',
                    'filters': ['require_debug_false'],
                    'class': 'django.utils.log.AdminEmailHandler'
                },
            },
            'loggers': {
                'django': {
                    'handlers': ['console'],
                    'propagate': True,
                },
                 'django.request': {
                    'handlers': ['console', 'mail_admins'],
                    'level': 'ERROR',
                    'propagate': True,
                },
                'testlogger': {
                    'handlers': ['console'],
                    'level': 'INFO',
                }
            }
        }
