from .base import *

DEBUG = False

ADMINS = [
    ('Ignatus Arkoh Amoah', 'ignis2a@gmail.com'),
]

ALLOWED_HOSTS = ['www.juvyboy.com', 'juvyboy.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config.get('DB_NAME'),
        'USER': config.get('DB_USER'),
        'PASSWORD': config.get('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}


# HTTPS settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
