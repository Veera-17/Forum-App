"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env_path = load_dotenv(os.path.join(BASE_DIR, '.env'))
load_dotenv(env_path)

# env_path = load_dotenv(os.path.join(BASE_DIR, '.env'))
# load_dotenv(env_path)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x$l$q1=cvnmr3g%jjl1(uu4(je^!cahf!r81v&)34+d9f164n_'
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
# DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'



ALLOWED_HOSTS = ['veeragokul.pythonanywhere.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'boards.apps.BoardsConfig',
    'accounts.apps.AccountsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'django.contrib.humanize',
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

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

LOGOUT_REDIRECT_URL = 'home'
LOGIN_REDIRECT_URL = 'home'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
LOGIN_URL = 'login'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Add the email host
EMAIL_HOST_USER = 'cecsharishv24@gmail.com'
EMAIL_HOST_PASSWORD = 'defa ghzv xgvp xwis'  # App password for Gmail
EMAIL_PORT = 587
EMAIL_USE_TLS = True

import dj_database_url

# DATABASE_URL = 'postgres://forum:Veera%4017@veeragokul.postgres.pythonanywhere-services.com:5432/forum'

# # Configure the default database using DATABASE_URL
# DATABASES = {
#     'default': dj_database_url.parse(DATABASE_URL, conn_max_age=500, conn_health_checks=True)
# }
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(
        conn_max_age=500,
        conn_health_checks=True,
    )

STATIC_ROOT = BASE_DIR / "staticfiles"

# Static file serving.
# https://whitenoise.readthedocs.io/en/stable/django.html#add-compression-and-caching-support
STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

CSRF_TRUSTED_ORIGINS = ['https://veeragokul.pythonanywhere.com']
