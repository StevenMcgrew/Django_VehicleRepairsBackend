from pathlib import Path


SECRET_KEY = 'dev_key'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vehicle_repairs_db',
        'USER': 'postgres',
        'PASSWORD': 'VoltageDrop0.0',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

BASE_DIR = Path(__file__).resolve().parent.parent.parent
STATIC_URL = '/static/'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'vehicle_repairs',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'django_filters',
]
