import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# =========================================================
# Django Core Settings
# =========================================================

DEBUG = False
SITE_ID = 1
ALLOWED_HOSTS = ["*"]
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

ADMIN_URL_KEY = os.environ.get('BACKEND_ADMIN_PATH', 'admin')
ADMIN_URL_PATH = '{}/'.format(ADMIN_URL_KEY)

# Application definition
# ---------------------------------------------------------

INSTALLED_APPS = (
    # Django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',

    # 3rd part apps
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',

    # Project apps
    'backend.api',
)

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Authentication
# ---------------------------------------------------------

AUTHENTICATION_BACKENDS = (
    # Required for login by username in Django admin
    'django.contrib.auth.backends.ModelBackend',
)

# AUTH_USER_MODEL = 'accounts.CustomUser'
# LOGIN_URL = '/accounts/login/'
# LOGIN_REDIRECT_URL = '/home'

# Sessions
# ---------------------------------------------------------

SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_SAVE_EVERY_REQUEST = True

# Security
# ---------------------------------------------------------

# SECURITY WARNING: Use unique key in production and keep it secret!
SECRET_KEY = '+^b03*zldz4fd!p%asz+(8u8b-0#6uw4eaex0xf$3w-km%)&2y'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Internationalization
# ---------------------------------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files
# ---------------------------------------------------------

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]

# Database
# ---------------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# =========================================================
# Third Party Apps Settings
# =========================================================


# Rest Framework
# ---------------------------------------------------------

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

# Djoser
# ---------------------------------------------------------

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SERIALIZERS': {},
}

# =========================================================
# Logging Settings
# =========================================================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(name)s: %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        }
    },
    'loggers': {
        # Django loggers
        'django': {
            'level': 'INFO',
            'handlers': ['console'],
        },
        # Backend logger
        'backend': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        }
    }
}