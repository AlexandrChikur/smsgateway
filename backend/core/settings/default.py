import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# =========================================================
# Django Core Settings
# =========================================================

DEBUG = False
SITE_ID = 1
ALLOWED_HOSTS = ["*"]
ADMINS = [
    # "name:password"
    "achikur:Aa12345",
]

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
    'channels',
    'drf_yasg',
    'djoser',

    # Project apps
    'accounts',
    'api',
    'web',
    'sms',

)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
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
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        'OPTIONS': {
            'min_length': 6,
        }
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

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

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

DEFAULT_PHONE_REGION = os.environ.get('BACKEND_PHONE_REGION', 'RU')

# Static files
# ---------------------------------------------------------


STATIC_URL = "/static/"
MEDIA_URL = "/media/"
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

CACHES = {
    "default": {
        "BACKEND": "redis_cache.RedisCache",
        "LOCATION": os.getenv("BACKEND_REDIS_URL",
                              (os.getenv("BACKEND_REDIS_HOST", '127.0.0.1'), os.getenv("BACKEND_REDIS_PORT", 6379))),
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
    ),
    'EXCEPTION_HANDLER': 'core.drf.exception_handler',
}

# Djoser
# ---------------------------------------------------------

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'PERMISSIONS': {
        "user_create": ["rest_framework.permissions.IsAdmin"],
    },
    'SERIALIZERS': {},
}

# Swagger
# ---------------------------------------------------------

SWAGGER_SETTINGS = {
    'LOGIN_URL': "/api/v1/api-auth/login/?next=/api/v1/swagger/",
    'LOGOUT_URL': "/api/v1/api-auth/logout/?next=/api/v1/swagger/",
    'validatorUrl': None,
}

# Channels
# ---------------------------------------------------------

ASGI_APPLICATION = "core.asgi.application"
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [os.getenv("BACKEND_REDIS_URL",
                                (os.getenv("BACKEND_REDIS_HOST", '127.0.0.1'), os.getenv("BACKEND_REDIS_PORT", 6379)))],
            "symmetric_encryption_keys": [SECRET_KEY],
        },
    },
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
