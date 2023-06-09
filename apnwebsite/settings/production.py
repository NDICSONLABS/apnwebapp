import os
import environ
import dj_database_url

from .base import *  # noqa


env = environ.Env()

environ.Env.read_env()

DEBUG = True #'RENDER' not in os.environ

ALLOWED_HOSTS = ["*"]

SECRET_KEY = os.environ.get('SECRET_KEY', default="django-insecure-zo$k*ovelw5z4fa1$-w3wxd=*fm+cykp4v6!2k*3kejd+s3p)i") # noqa

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME') # noqa

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(env("DATABASES_URL"))
}

try:
    from .base import * # noqa
    if RENDER_EXTERNAL_HOSTNAME:
        ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME) # noqa
except ImportError:
    pass
