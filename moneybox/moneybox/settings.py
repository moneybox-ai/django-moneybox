import json
import os
import tink

from dotenv import load_dotenv
from tink import cleartext_keyset_handle
from tink import daead
from pathlib import Path

daead.register()
load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET", "secret")

DEBUG = os.getenv("DJANGO_DEBUG", "True") == "True"

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "users",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "api",
    "wallet",
    "core",
    "drf_spectacular",
    "drf_generators",
    "django_celery_beat",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "moneybox.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "moneybox.wsgi.application"

LOCAL_ENV = "local"

ENV = os.getenv("ENV", LOCAL_ENV)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_DB_HOST", "db"),
        "PORT": os.getenv("POSTGRES_DB_PORT", "5342"),
    }
}

AUTH_USER_MODEL = "users.User"

AUTH_HEADER = "Authorization"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 15,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "api.authentication.APIAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "api.permissions.IsAuthenticated",
    ],
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
    },
}


SPECTACULAR_SETTINGS = {
    "TITLE": "MoneyBox",
    "DESCRIPTION": (
        "MoneyBox will help you better understand your finances, "
        "improve financial literacy, and achieve financial goals."
    ),
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "api.authentication.APIAuthentication",
    ],
    "SERVE_PERMISSIONS": ["rest_framework.permissions.AllowAny"],
    "SERVE_AUTHENTICATION": None,
}
# celery
CELERY_BEAT_SCHEDULER = os.getenv("CELERY_BEAT_SCHEDULER", "django_celery_beat.schedulers:DatabaseScheduler")
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
# cbr
CBR_TIMEOUT = 10
CBR_URL = "https://cbr.ru/scripts/XML_daily.asp"
# coingecko
COINGECKO_TIMEOUT = 10
COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price?ids={crypto_currencies}&vs_currencies={fiat_currency}"
# encoding
PRE_KEYSET = {
    "key": [
        {
            "keyData": {
                "keyMaterialType": os.getenv("KEY_MATERIAL_TYPE", "SYMMETRIC"),
                "typeUrl": os.getenv("TYPE_URL", "type.googleapis.com/google.crypto.tink.AesSivKey"),
                "value": os.getenv(
                    "VALUE", "EkDseJb9CSmxFJJ66dRrwQXN+ToxcBxJC/GPwhFfTYHREMfgTX2t52RpDQ6u29TdintRxJm8RLaMMvmjmDao1Lpu"
                ),
            },
            "keyId": os.getenv("KEY_ID", 2021474508),
            "outputPrefixType": os.getenv("OUTPUT_PREFIX_TYPE", "TINK"),
            "status": os.getenv("STATUS", "ENABLED"),
        }
    ],
    "primaryKeyId": os.getenv("PRIMARY_KEY_ID", 2021474508),
}
KEYSET = json.dumps(PRE_KEYSET, indent=4)
KEYSET_HANDLE = cleartext_keyset_handle.read(tink.JsonKeysetReader(KEYSET))
PRIMITIVE = KEYSET_HANDLE.primitive(daead.DeterministicAead)
