# Import all default settings.
from .settings import *

import django_heroku

# Activate Django-Heroku.
django_heroku.settings(locals())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dd5c6t4965hkoi',
        'USER': 'uwpedxnkvyfmsv',
        'PASSWORD': 'f2bcc166eca0664d734d4f8dbe538ca9d0559307869925c799e8830fa3dedbed',
        'HOST': 'ec2-54-225-228-142.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
