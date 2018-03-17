"""
Django settings for xcourriel project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import getconf
CONFIG = getconf.ConfigGetter('xcourriel', [os.path.join(BASE_DIR, 'local_settings.ini')])

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CONFIG.getstr('django.secret_key', 'Dev only!!')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'platal',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'xcourriel.urls'

WSGI_APPLICATION = 'xcourriel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'platal': {
        'ENGINE': 'django.db.backends.' + CONFIG.getstr('plataldb.engine', 'sqlite3'),
        'NAME': CONFIG.getstr('plataldb.name', 'x5dat'),
        'USER': CONFIG.getstr('plataldb.user', 'web'),
        'PASSWORD': CONFIG.getstr('plataldb.password'),
        'HOST': CONFIG.getstr('plataldb.host', '127.0.0.1'),
        'PORT': CONFIG.getstr('plataldb.port', '3306'),
    },
}

# Do not manage MySQL databases but manage SQLite ones for tests and local development
PLATAL_MANAGED = (DATABASES['platal']['ENGINE'] == 'django.db.backends.sqlite3')

DATABASE_ROUTERS = ['platal.dbrouter.PlatalRouter']

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
