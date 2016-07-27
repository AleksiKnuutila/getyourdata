from .settings import *

import os

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'getyourdatadevdb',
        'USER': 'getyourdatadevuser',
        'PASSWORD': 'getyourdatadevpwd',
        'HOST': 'localhost',
        'PORT': '',
    }
}

AUTH_PASSWORD_VALIDATORS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if TESTING:
    EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

os.environ["RECAPTCHA_TESTING"] = 'True'

PIPELINE['PIPELINE_ENABLED'] = False
