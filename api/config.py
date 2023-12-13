import os

class AppConfig(object):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')