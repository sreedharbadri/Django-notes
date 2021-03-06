"""
Django settings for AddressBook project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# /home/key2gyaan/Documents/git_repositories/tuxfux-hlp-notes/Django-notes/Batch-201/src
print BASE_DIR


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ps-vfc(!*fgy!+cx&=^#&$z)#=06&%q+xg3$w*&fndghn^0nk9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    # Django inbuild apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  # this is the app for laying our your static files.
    # custom apps
    'newtest_app',
    'address',
    # installed apps
    'crispy_forms',
    'registration',
     'fontawesome',  # https://github.com/redouane/django-fontawesome
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'AddressBook.urls'


# Day 6
# creating a templates folder outside apps. - see day6_notes : postmortem notes for more details.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR + "/templates"],
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

WSGI_APPLICATION = 'AddressBook.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Day 6:
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# Day 7
# https://docs.djangoproject.com/en/1.8/howto/static-files/#configuring-static-files
# order of searching for static files : project_local(STATICFILES_DIRS) =>> order of apps in setting.py
# INSTALLED_APPS - newtest_app(+static folder)
# INSTALLED_APP - address(+static folder) 
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,"project_local"),
    )

# static_root
# https://docs.djangoproject.com/en/1.8/howto/static-files/#deployment
STATIC_ROOT = os.path.join(BASE_DIR,"project_prod")

# Day 8 
# Email setup - gmail.com
# smtp server and use can provide username and password.
# https://docs.djangoproject.com/en/1.10/topics/email/

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'tuxfux.django@gmail.com'
EMAIL_HOST_PASSWORD = 'tuxfux.django123'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Django registration redux settings.
LOGIN_REDIRECT_URL="/"
ACCOUNT_ACTIVATION_DAYS=7