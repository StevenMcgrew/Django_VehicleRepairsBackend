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
