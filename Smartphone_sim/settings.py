"""
Django settings for Smartphone_Sim project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from django.core.management import utils
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-q8_iga)!#^(r9!q#pw!ugnuhtzsqzqi4w%fz+0d79@j2j_8l%4"
TWILIO_AUTH_TOKEN = "e0501fffd7c39df186f93d2f4aea8bed"
TWILIO_AUTH_SID = "ACc52255411661040dab50f0f944e722e5"
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','www.kevinsproject.xyz','kevinsproject.xyz','23.239.15.144']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'Home',
    'Communication',
    'Miscellaneous',
    'Social_Media',
    'Games'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Smartphone_sim.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"Templates")],
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

WSGI_APPLICATION = 'Smartphone_sim.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
MEDIA_URL = '/App_Files/'
MEDIA_ROOT = os.path.join(BASE_DIR,'App_Files')
#STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
LOGOUT_REDIRECT_URL = "Login"
LOGIN_REDIRECT_URL = 'Home'
LOGIN_URL = 'Login'
EMAIL_HOST = '23.239.15.144'
EMAIL_HOST_USER = "kevinsproject0@gmail.com"
EMAIL_HOST_PASSWORD = "kevinsproject123$"
EMAIL_PORT = 465
EMAIL_USE_SSL = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
