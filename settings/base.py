"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from datetime import timedelta # used for JWT settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']

# Application definition
INSTALLED_APPS = [
  # Project Apps Listed First
  'users.apps.UserAppConfig',

  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django_extensions',
  'graphene_django',
  'import_export',
  'simple_history',
  'corsheaders',
  'health_check',
  'health_check.db',
]

GRAPHENE = {
  'SCHEMA': 'server.schema.schema', # Where your Graphene schema lives
  'MIDDLEWARE': [ # Provides info.context.user to queries and mutations
    'graphql_jwt.middleware.JSONWebTokenMiddleware',
  ],
}

AUTHENTICATION_BACKENDS = [
  'graphql_jwt.backends.JSONWebTokenBackend',
  'django.contrib.auth.backends.ModelBackend',
]

GRAPHQL_JWT = {
  'JWT_VERIFY_EXPIRATION': False, # Turned off for easy graphql testing
  'JWT_EXPIRATION_DELTA': timedelta(minutes=5),
  'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
}

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'handlers': {
    'console': {
      'class': 'logging.StreamHandler',
    },
  },
  'root': {
    'handlers': ['console'],
    'level': 'WARNING',
  },
  'loggers': {
    'django': {
      'handlers': ['console'],
      'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
      'propagate': False,
    },
    'django.db.backends': {
      'level': os.getenv('DJANGO_DB_LOG_LEVEL', 'ERROR'),
      'handlers': ['console'],
    },
  },
}

MIDDLEWARE = [
  'django.middleware.gzip.GZipMiddleware',
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'server.urls'

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

WSGI_APPLICATION = 'server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# Should be updated with your database info and credentials
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ['DATABASE_NAME'],
    'USER': os.environ['DATABASE_USER'],
    'PASSWORD': os.environ['DATABASE_PASSWORD'],
    'HOST': os.environ['DATABASE_HOST'],
    'PORT': os.environ['DATABASE_PORT']
  }
}

# Tells django to use custom user model for authentication
AUTH_USER_MODEL = 'users.User'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

CORS_ALLOWED_ORIGINS = [
  "http://localhost:3000",
  "http://127.0.0.1:3000"
]
