from pathlib import Path
import os
import dj_database_url
import django_heroku
from django.contrib.messages import constants as messages


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY', 'django-insecure-o47&kilmpi3vgmw*u29c3yoip(t8^0&)yp%squ)u3!j6ianghk')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if str(os.environ.get(
    "DJANGO_DEBUG", "False")) == "True" else False
DEV = False
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'django.contrib.humanize',

    # apps
    'products',
    'order',
    'checkout',
    'user',
    'base',
    'storages',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'imanClothing.urls'

AUTH_USER_MODEL = 'user.User'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'base.cart_count_context.get_cart_count',
            ],
        },
    },
]

WSGI_APPLICATION = 'imanClothing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
if DEV:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    DEBUG = True
    MEDIA_URL = '/media/'
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / 'static'
    ALLOWED_HOSTS = ["*"]
else:
    if DEBUG == True:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
        MEDIA_URL = '/media/'
        STATIC_URL = '/static/'
        STATIC_ROOT = BASE_DIR / 'static'
        ALLOWED_HOSTS = ["*"]
    else:
        DATABASES = {
            'default': dj_database_url.config()
        }
        # -------------------------------------------------------------------------------------------------
        # allowned hosts
        ALLOWED_HOSTS = ["www.imanclothing.net",
                         "imanclothing.net", "admin.imanclothing.net", ]

        # ssl forcing
        SECURE_SSL_REDIRECT = True

        # static and media files
        AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
        AWS_S3_REGION_NAME = os.environ.get(
            "AWS_S3_REGION_NAME")  # e.g. us-east-2
        AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
        AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

        AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

        STATICFILES_LOCATION = 'static'
        STATICFILES_STORAGE = 'custom_storages.StaticStorage'

        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'

        # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3Boto3Storage'
        MEDIAFILES_LOCATION = 'media'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

        # django_heroku.settings(locals(), staticfiles=False)


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

LOGIN_URL = "/account/login"

# ---------------------------------------------------------------------------------------------------------


# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# payment gateaway
PAYMENT_GATEAWAY_URL = "https://api.paystack.co/transaction/initialize"
PAYMENT_VERIFICATION_URL = " https://api.paystack.co/transaction/verify/"
PAYMENT_GATEAWAY_SECRET_KEY = os.environ.get(
    "PAYMENT_GATEAWAY_SECRET_KEY") if not DEV else "sk_test_a6ab34905d1976de1021fd6ff3ec79b9305b17e5"
PAYMENT_GATEAWAY_PUBLIC_KEY = os.environ.get(
    "PAYMENT_GATEAWAY_PUBLIC_KEY") if not DEV else "pk_test_4113a8e663d336eb320548c07ea77b4f06ce8ad8"

REDIRECT_URL = "https://www.imanclothing.net/checkout/verify"
# REDIRECT_URL = "http://127.0.0.1:8000/checkout/verify"
