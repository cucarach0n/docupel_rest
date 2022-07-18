from .base import *
from decouple import config
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DATA_BASE'),
        'USER': config('DATA_BASE_USER'),
        'PASSWORD': config('DATA_BASE_PASSWORD'),
        'HOST': config('DATA_BASE_HOST'),
        'PORT': '',
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'