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
SECRET_KEY = secrets.get(
    "SECRET_KEY", '9n2k6si$nzvbrl*k(0!*x@n#(m#@rx1jd_x4q0+e1uip7!$=t#')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Are we running tests
TESTING = False

SITE_ID = 1

TEST_RUNNER = "getyourdata.testrunner.TestSuiteRunner"


ALLOWED_HOSTS = secrets.get("ALLOWED_HOSTS", [])

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
    'django.contrib.sites',
    'django.contrib.flatpages',
    'tinymce',
    'rosetta',
    'rest_framework',
    'debug_toolbar',
    'django_extensions',
    'captcha',
    'pipeline',

    'getyourdata',
    'home',
    'organization',
    'data_request',
    'feedback',

    # We're overriding bootstrap3's default templates, which is why it's loaded
    # last
    'bootstrap3',
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
    'pipeline.middleware.MinifyHTMLMiddleware',
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
                'feedback.context_processors.feedback_form',
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
        'NAME': secrets.get("DB_NAME", "getyourdatadb"),
        'USER': secrets.get("DB_USER", "getyourdatauser"),
        'PASSWORD': secrets.get("DB_PASS", "getyourdatapwd"),
        'HOST': secrets.get("DB_HOST", "localhost"),
        'PORT': '',
    }
}

# Cache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': secrets.get("MEMCACHED_LOCATION", "127.0.0.1:11211")
    }
}

MIGRATION_MODULES = {
    "flatpages": "getyourdata.migrations.flatpages",
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

# Email settings

EMAIL_HOST = secrets.get("EMAIL_HOST", "")
EMAIL_HOST_PASSWORD = secrets.get("EMAIL_HOST_PASSWORD", "")
EMAIL_HOST_USER = secrets.get("EMAIL_HOST_USER", "")
EMAIL_PORT = secrets.get("EMAIL_PORT", 25)
EMAIL_USE_TLS = secrets.get("EMAIL_USE_TLS", False)
EMAIL_USE_SSL = secrets.get("EMAIL_USE_SSL", False)

NOREPLY_EMAIL_ADDRESS = "noreply@getyourdata.org"

# reCAPTCHA settings

RECAPTCHA_PUBLIC_KEY = secrets.get(
    "RECAPTCHA_PUBLIC_KEY", "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI")
RECAPTCHA_PRIVATE_KEY = secrets.get(
    "RECAPTCHA_PRIVATE_KEY", "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe")
# Use the new "No Captcha" CAPTCHA
NOCAPTCHA = secrets.get("NOCAPTCHA", True)
RECAPTCHA_USE_SSL = secrets.get("RECAPTCHA_USE_SSL", True)

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATIC_ROOT = secrets.get("STATIC_ROOT", '%s/site_media' % os.getcwd())

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    #'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.FileSystemFinder',
    'pipeline.finders.AppDirectoriesFinder',
    'pipeline.finders.CachedFileFinder',
    'pipeline.finders.PipelineFinder',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

PIPELINE = {
    'PIPELINE_ENABLED': True,
    'CSS_COMPRESSOR': 'pipeline.compressors.NoopCompressor',
    'JS_COMPRESSOR': 'pipeline.compressors.NoopCompressor',
    'STYLESHEETS': {
        'base_style': {
            'source_filenames': (
                'css/bootstrap-overrides.css',
                'css/getyourdata.css',
                'css/chosen.min.css',
            ),
            'output_filename': 'css/base_style.css',
        },
        'star_rating': {
            'source_filenames': (
                'css/star-rating.min.css',
            ),
            'output_filename': 'css/star_rating.css',
        },
    },
    'JAVASCRIPT': {
        'base_script': {
            'source_filenames': (
                'js/chosen.jquery.min.js',
                'js/handlebars.min.js',
            ),
            'output_filename': 'js/base_script.js',
        },
        'star_rating': {
            'source_filenames': (
                'js/star-rating.min.js',
            ),
            'output_filename': 'js/star_rating.js',
        },
    }
}

# Media

MEDIA_URL = '/media/'

MEDIA_ROOT = secrets.get("MEDIA_ROOT", '%s/media' % os.getcwd())

# Session

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# Grappelli

GRAPPELLI_ADMIN_TITLE = 'GetYourData admin'

# TinyMCE

TINYMCE_DEFAULT_CONFIG = {
    'valid_elements': (
        "a[*],strong/b[*],em[*],span[*],"
        "address[*],pre[*],br[*],p[*],ul[*],ol[*],li[*],table[*],tbody[*],tr[*],td[*],"
        "th[*],h1[*],h2[*],h3[*],h4[*],h5[*],h6[*],img[*],iframe[*],video[*],audio[*],"
        "object[*],param[*],div[*],small[*],hr[*],style[*],script[*],link[*],strong[*],"
    ),
    'content_css':  "//maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css,"
                    "/static/css/getyourdata.css,"
                    "/static/css/chosen.min.css,"
                    "/static/css/bootstrap-overrides.css,",
    'plugins': (
        "style,media,table,spellchecker,paste,"
        "searchreplace,preview,inlinepopups,advlink"
    ),
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'plugin_preview_width': 1200,
    'plugin_preview_height': 1000,
    'width': 1200,
    'height': 1000,
    'theme': "advanced",
    'toolbar_location': "top",
    'theme_advanced_buttons1': (
        "bold,italic,underline,separator,bullist,separator,outdent,"
        "indent,separator,undo,redo,separator,fontsizeselect,formatselect,"
        "separator,link,image,media,code,preview"
    ),
    'theme_advanced_buttons2': "table,tablecontrols",
    'convert_urls': False,
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

# Pagination

ORGANIZATIONS_PER_PAGE = 15

COMMENTS_PER_PAGE = 10
