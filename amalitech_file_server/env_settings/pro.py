import os

SECRET_KEY = os.environ['SECRET_KEY'] | ''

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


ACCOUNT_ACTIVATION_DAYS = 7
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ['email_user'] | ''
EMAIL_HOST_PASSWORD = os.environ['email_password'] | ''
EMAIL_PORT = 587