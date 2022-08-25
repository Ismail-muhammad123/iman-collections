from pathlib import Path
import os
import dj_database_url
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o47&kilmpi3vgmw*u29c3yoip(t8^0&)yp%squ)u3!j6ianghk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


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

ROOT_URLCONF = 'fashionaWeb.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'fashionaWeb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if DEBUG else {

        'ENGINE': 'ec2-3-219-229-143.compute-1.amazonaws.com',

        'NAME': 'd5m40hju55snlc',

        'USER': 'gspsdvfoogikru',

        'PASSWORD': '429aae81cbc58fadd235ac8d3e302c1c999d5052ab5d98fe35e4e0de7838b1a2',

        'HOST': 'postgres://gspsdvfoogikru:429aae81cbc58fadd235ac8d3e302c1c999d5052ab5d98fe35e4e0de7838b1a2@ec2-3-219-229-143.compute-1.amazonaws.com:5432/d5m40hju55snlc',

        'PORT': '5432',
    }
}


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


# -------------------------------------------------------------------------------------------------

AWS_STORAGE_BUCKET_NAME = 'iman-clothing-staticfiles'
AWS_S3_REGION_NAME = 'eu-west-3'  # e.g. us-east-2
AWS_ACCESS_KEY_ID = 'AKIAQXLZN6YAVWBA7JFQ'
AWS_SECRET_ACCESS_KEY = '9WVF/M+2s7pWo8QowM/SvynUBLgHs+thMkGvebnr'

# Tell django-storages the domain to use to refer to static files.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# Tell the staticfiles app to use S3Boto3 storage when writing the collected static files (when
# you run `collectstatic`).

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'


# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3Boto3Storage'
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

# ---------------------------------------------------------------------------------------------------------

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# payment gateaway
PAYMENT_GATEAWAY_URL = "https://api.flutterwave.com/v3/payments"
PAYMENT_GATEAWAY_SECRET_KEY = "FLWSECK_TEST-64787ade1481e5435e25c1a626409bc7-X"


# django_heroku.settings(locals())
