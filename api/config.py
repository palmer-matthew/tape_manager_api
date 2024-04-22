import os

class ApiConfig(object):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    PORT = 8080
    HOST = '0.0.0.0'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://username:password@localhost/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_ERROR_404_HELP = False

class DevApiConfig(ApiConfig):
    DEBUG = True
    DEVELOPMENT = True

class ProdApiConfig(ApiConfig):
    DEBUG = False
    DEVELOPMENT = False