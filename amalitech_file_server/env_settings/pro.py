import os

from amalitech_file_server.common import DATABASES

SECRET_KEY = os.getenv('SECRET_KEY','')

DEBUG = False
ALLOWED_HOSTS = ['Goldberg.pythonanywhere.com']

DATABASES['default']['NAME'] = 'Goldberg$amalitech'


# ACCOUNT_ACTIVATION_DAYS = 2
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
PASSWORD_RESET_TIMEOUT_DAYS = 1

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.getenv('EMAIL_USER','')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD','')
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'