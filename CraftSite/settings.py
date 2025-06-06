"""
Django settings for P2CraftProject project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print("This is base directory: ", BASE_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hsux8ul=lbsjb+&f_wu!sqb_)xqk0f(8eaeh=&w91ophumtyf5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

import os

# Google Maps API Key
# GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY', 'AIzaSyD7FSNV6yrCzpa3UNvWVFj0peDy2oKYUuA') # google maps api thing
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY', 'AIzaSyDNAvLo-Yzk7JNBVfIjuWipvTlx7MWWHtg')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'location_field.apps.DefaultConfig',
    # 'django.contrib.gis', # This guy gives an error, so imma try the google maps variation

    'Crafts',
    'Media',
    'accounts',
    'chatBot',

]

LOCATION_FIELD = {
    'map.provider': 'google',
    'map.zoom': 13,
    'map.center': {'lat': 0, 'lng': 0},
    'provider.google.api': '//maps.googleapis.com/maps/api/js?key=AIzaSyD7FSNV6yrCzpa3UNvWVFj0peDy2oKYUuA',  #TODO PLEASE CHANGE THIS!
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

ROOT_URLCONF = 'CraftSite.urls'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Gmail SMTP server
EMAIL_PORT = 587  # Use port 587 for secure connections (TLS)
EMAIL_USE_TLS = True  # Mandatory for Outlook and Gmail
EMAIL_HOST_USER = 'arkpianist3@gmail.com' # os.getenv('EMAIL_HOST_USER')  # Your Outlook email address
EMAIL_HOST_PASSWORD = 'ryzlfdgbscdejkfu' # os.getenv('EMAIL_HOST_PASSWORD')  # App password for Outlook
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER # os.getenv('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER)  # Default "from" email

TEMPLATES_ACCOUNTS = os.path.join(BASE_DIR, 'accounts/templates')
TEMPLATES_MEDIA = os.path.join(BASE_DIR, 'Media/templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'Crafts/templates'),
            os.path.join(BASE_DIR, 'CraftSite/templates'),  # Add this line to include CraftSite templates
            TEMPLATES_ACCOUNTS,
            TEMPLATES_MEDIA,  # need comma if you add more templates
            os.path.join(BASE_DIR, 'Media_images')
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

WSGI_APPLICATION = 'CraftSite.wsgi.application'


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

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# need to register the folder containing css file and static files to use them 
STATICFILES_DIRS = [
    BASE_DIR / 'CraftSite/static/',
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
YOUTUBE_API_KEY = "AIzaSyBI8SI8Dlykx_e8PyhK5YzTiLX5Nm3aBWs"  # Replace with your actual API key

OPENAI_API_KEY = config('OPENAI_API_KEY')

