"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from django.core.exceptions import ImproperlyConfigured
from pathlib import Path
import dj_database_url


# Helper function to get environment variables safely
def get_env_variable(var_name, default=None):
    try:
        return os.environ[var_name]
    except KeyError:
        if default is not None:
            return default
        raise ImproperlyConfigured(f"The environment variable {var_name} is not set.")


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable('SECRET_KEY', 'your-fallback-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env_variable('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = get_env_variable('ALLOWED_HOSTS', '').split(',')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'moscraciun',
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

ROOT_URLCONF = 'api.urls'

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

WSGI_APPLICATION = 'api.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# Database Configuration
DATABASES = {
    'default': dj_database_url.parse(get_env_variable('DATABASE_URL', default="sqlite:///db.sqlite3"))
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

# URL for serving static files
STATIC_URL = '/static/'

# Directory for storing static files in the project
STATICFILES_DIRS = [BASE_DIR / "static"]

# Directory where static files will be collected for production (e.g., during `collectstatic`)
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media Files Configuration
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Cloudcube-specific environment variables
CLOUDCUBE_URL = get_env_variable('CLOUDCUBE_URL')  # Provided by Heroku's Cloudcube add-on
AWS_ACCESS_KEY_ID = get_env_variable('CLOUDCUBE_ACCESS_KEY_ID')  # Your Cloudcube Access Key
AWS_SECRET_ACCESS_KEY = get_env_variable('CLOUDCUBE_SECRET_ACCESS_KEY')  # Your Cloudcube Secret Key

# Parse the Cloudcube URL
CLOUDCUBE_BUCKET_NAME = CLOUDCUBE_URL.split('/')[-2]  # Extract bucket name from URL
CLOUDCUBE_MEDIA_ROOT = CLOUDCUBE_URL.split('/')[-1]   # Extract folder prefix from URL
AWS_STORAGE_BUCKET_NAME = CLOUDCUBE_BUCKET_NAME

AWS_S3_ENDPOINT_URL = 'https://s3.amazonaws.com'  # S3 default endpoint for Cloudcube
AWS_QUERYSTRING_AUTH = False  # Set to False if you want public URLs for media files

# Media URL configuration
MEDIA_URL = f'{CLOUDCUBE_URL}/'
