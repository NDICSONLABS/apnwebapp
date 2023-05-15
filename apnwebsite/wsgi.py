"""
WSGI config for apnwebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

DEBUG = 'RENDER' not in os.environ

if not DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apnwebsite.settings.production") # noqa
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apnwebsite.settings.dev")

application = get_wsgi_application()
