"""
Django settings for tango_with_django_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_DIRS, STATICFILES_DIRS

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# BASE_DIR = os.path.join(BASE_DIR, os.pardir)
# BASE_DIR = os.path.abspath(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i%gt3plkzg0*lyvsx#nn@4+!1xr7=g(+fxc3(v8j9tnwm8a9(z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'rango',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tango_with_django_project.urls'

WSGI_APPLICATION = 'tango_with_django_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


DATABASE_PATH = os.path.join(BASE_DIR, 'rango.sqlite3')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_PATH,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_PATH = os.path.join(BASE_DIR,'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    STATIC_PATH,
)

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

