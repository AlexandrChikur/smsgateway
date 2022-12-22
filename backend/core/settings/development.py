import os

from .default import *  # noqa

# =========================================================
# Django Core Settings
# =========================================================

DEBUG = True
ALLOWED_HOSTS = ['*']

# Application definition
# ---------------------------------------------------------

INSTALLED_APPS += (  # noqa: F405
    'debug_toolbar',
)

MIDDLEWARE += [  # noqa: F405
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Static files
# ---------------------------------------------------------

STATIC_ROOT = ''

# Database
# ---------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('BACKEND_DB_NAME', 'postgres'),
        'USER': os.environ.get('BACKEND_DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('BACKEND_DB_PASSWORD', 'postgres'),
        'HOST': os.environ.get('BACKEND_DB_HOST', 'localhost'),
        'PORT': int(os.environ.get('BACKEND_DB_PORT', 5432)),
        'CONN_MAX_AGE': None
    }
}


# Debug Toolbar
# ---------------------------------------------------------
DEBUG_TOOLBAR_PATCH_SETTINGS = False

# =========================================================
# Backend Settings
# =========================================================

SITE_ENV = 'DEV'
