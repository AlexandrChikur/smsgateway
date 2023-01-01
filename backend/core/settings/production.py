import os

import dj_database_url

from .default import *  # noqa


def _read_secret_key(settings_dir='/etc/sms-gateway/backend'):
    """
    Reads secret key from environment variable, otherwise from SECRET_KEY
    file in settings directory.
    In case secret key cannot be read, function returns None, which
    causes django configuration exception.
    :param settings_dir: Settings directory, default: '/etc/sms-gateway/backend'.
    :return: Secret key string, if available, None otherwise.
    """
    try:
        return os.environ['BACKEND_SECRET_KEY']
    except KeyError:
        pass

    try:
        with open(os.path.join(settings_dir, 'SECRET_KEY')) as fp:
            return fp.read().strip()
    except IOError:
        return None


# =========================================================
# Django Core Settings
# =========================================================

DEBUG = False
ALLOWED_HOSTS = os.environ.get('BACKEND_ALLOWED_HOSTS', '*').split(',')
ADMINS = os.getenv("BACKEND_ADMINS", '').split(',')  # Provided as comma separated `name:pwd` string

# Database
# ---------------------------------------------------------

DATABASES = {}

if os.environ.get('BACKEND_DB_URL'):
    DATABASES['default'] = dj_database_url.config(
        env='BACKEND_DB_URL', conn_max_age=0)
else:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('BACKEND_DB_NAME', 'smsgateway'),
        'USER': os.environ.get('BACKEND_DB_USER', 'smsgateway'),
        'PASSWORD': os.environ.get('BACKEND_DB_PASSWORD', ''),
        'HOST': os.environ.get('BACKEND_DB_HOST', ''),
        'PORT': int(os.environ.get('BACKEND_DB_PORT', 5432)),
        'CONN_MAX_AGE': 0,
    }

# Static files
# ---------------------------------------------------------

STATIC_ROOT = '/usr/share/sms-gateway/public/static'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Security
# ---------------------------------------------------------

SECRET_KEY = _read_secret_key()

# =========================================================
# Backend Settings
# =========================================================

SITE_ENV = 'PROD'

# =========================================================
# Logging Settings
# =========================================================

LOGGING['handlers']['console'] = {
    'level': 'INFO',
    'class': 'logging.StreamHandler',
    'filters': ['request_id'],
    'formatter': 'json',
}

LOGGING['loggers']['backend'] = {
    'level': 'WARNING',
    'handlers': ['console'],
    'propagate': False,
}
