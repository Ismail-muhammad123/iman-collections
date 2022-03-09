import os
import dj_database_url

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'www.fashionacollections.com',
                 'fashionacollections.com']

AUTH_USER_MODEL = 'user.Account'

STATIC_ROOT = '/static/'

LOGIN_URL = '/user/login'


# Application definition

INSTALLED_APPS = [
    'user',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    "django.contrib.postgres",

    'products',
    'cart',
    'order',
    'payment',

    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fashionaWeb.urls'

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
                'products.context_processor.add_categories'
            ],
        },
    },
]

WSGI_APPLICATION = 'fashionaWeb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

if DEBUG:
    DATABASES['default'] = dj_database_url.config(
        conn_max_age=600, ssl_require=True)
else:
    DATABASES['default'] = dj_database_url.config(
        default='postgres://rrzltolgujedps:e503c5e717fd97c73fd5df219b56c1272ee12b9271c3f2b0ca48a71eba066d61@ec2-54-208-17-82.compute-1.amazonaws.com:5432/d3r0oqm6iptpjv')

# DATABASES['default'] = dj_database_url.config(
#     default='postgres://rrzltolgujedps:e503c5e717fd97c73fd5df219b56c1272ee12b9271c3f2b0ca48a71eba066d61@ec2-54-208-17-82.compute-1.amazonaws.com:5432/d3r0oqm6iptpjv')

SECRET_KEY = 'bjgvnbjihuio47&kilmpi3vgmw*u29c3yoip(t8^0&)yp%squ)u3!j6ianghk'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

AWS_ACCESS_KEY_ID = 'AKIAQXLZN6YA4RPUTUG3'
AWS_SECRET_ACCESS_KEY = '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'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = 'fashiona-store'
AWS_S3_REGION_NAME = 'us-east-2'


# payment gataway: paystack
PAYSTACK_SECRET_KEY = 'sk_live_3daa8d46aa673b474e6324f991318fe857310a7e'


# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'fashionaMailApi'
EMAIL_HOST_PASSWORD = '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'
EMAIL_USE_TLS = True


SERVER_EMAIL = 'report@fashiona.net'

ADMINS = [
    ("Ismail Muhammad", "ismaeelmuhammad123@gmail.com")
]

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
