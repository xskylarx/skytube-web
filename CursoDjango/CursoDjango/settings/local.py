__author__ = 'soporte'
from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': Path.join(BASE_DIR, 'db.sqlite3'),
    }
}


STATIC_URL = '/static/'