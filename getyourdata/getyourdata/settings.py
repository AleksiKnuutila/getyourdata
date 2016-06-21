"""
Django settings for getyourdata project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Import secrets for production environment if they exist
try:
    from getyourdata import secrets
    secrets = secrets.SECRETS
except ImportError:
    secrets = {}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets["SECRET_KEY"] if 'SECRET_KEY' in secrets else \
             '9n2k6si$nzvbrl*k(0!*x@n#(m#@rx1jd_x4q0+e1uip7!$=t#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Are we running tests
TESTING = False

TEST_RUNNER = "getyourdata.testrunner.TestSuiteRunner"


ALLOWED_HOSTS = secrets["ALLOWED_HOSTS"] if 'ALLOWED_HOSTS' in secrets else []

DEBUG = False

# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'tinymce',
    'rosetta',
    'rest_framework',

    'getyourdata',
    'home',
    'organization',
    'data_request',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'getyourdata.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

BOOTSTRAP3 = {
    'include_jquery': True
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication'   
    ],

    'PAGE_SIZE': 15,
}

WSGI_APPLICATION = 'getyourdata.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': secrets["DB_NAME"] if 'DB_NAME' in secrets else 'getyourdatadb',
        'USER': secrets["DB_USER"] if 'DB_USER' in secrets else 'getyourdatauser',
        'PASSWORD': secrets["DB_PASS"] if 'DB_PASS' in
                    secrets else 'getyourdatapwd',
        'HOST': secrets["DB_HOST"] if 'DB_HOST' in
                secrets else 'localhost',
        'PORT': '',
    }
}

# Cache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': secrets["MEMCACHED_LOCATION"]
                    if 'MEMCACHED_LOCATION' in secrets else '127.0.0.1:11211',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', _('English')),
    ('fi', _('Finnish')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = secrets["STATIC_ROOT"] if "STATIC_ROOT" in secrets else \
              '%s/site_media' % os.getcwd()

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Media

MEDIA_URL = '/media/'

MEDIA_ROOT = secrets["MEDIA_ROOT"] if "MEDIA_ROOT" in secrets else \
             '%s/media' % os.getcwd()

# Session

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# Grappelli

GRAPPELLI_ADMIN_TITLE = 'GetYourData admin'

# TinyMCE

TINYMCE_DEFAULT_CONFIG = {
    'valid_elements': (
        "a[href|target=_blank],strong/b,em,span[*],"
        "address,pre,br,#p[*],ul,ol,li,table[*],tbody[*],tr[*],td[*],"
        "th[*],h1,h2,h3,h4,h5,h6,img[*],iframe[*],video[*],audio[*],"
        "object[*],param[*],div[*]"
    ),
    'plugins': (
        "style,media,table,spellchecker,paste,"
        "searchreplace,preview,inlinepopups,advlink"
    ),
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'plugin_preview_width': 607,
    'width': 1000,
    'height': 800,
    'theme': "advanced",
    'toolbar_location': "top",
    'theme_advanced_buttons1': (
        "bold,italic,underline,separator,bullist,separator,outdent,"
        "indent,separator,undo,redo,separator,fontsizeselect,formatselect,"
        "separator,link,image,media,code,preview"
    ),
    'theme_advanced_buttons2': "table,tablecontrols",
}

TINYMCE_COMPRESSOR = False

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '%s/logs/error_log.txt' % BASE_DIR,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
