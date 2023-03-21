import os
from app import ENV_VARIABLES

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_HEADERS = 'Content-Type'
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024 #50MB file limit
    
    # Settings from https://stackoverflow.com/questions/58866560/flask-sqlalchemy-pool-pre-ping-only-working-sometimes
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 30,
        # 'pool_recycle': 60 * 60,
        'pool_recycle': 600, # experimental
        'pool_timeout' : 300,
        'pool_pre_ping': True,
        'max_overflow' : 15
    }


class LocalConfig(Config):
    DEBUG = True
    DB_NAME = ENV_VARIABLES['DB_LOCAL_NAME']
    DB_USERNAME = ENV_VARIABLES['DB_LOCAL_USER']
    DB_PASSWORD = ENV_VARIABLES['DB_LOCAL_PASS']
    IP = 'localhost'
    PORT = ENV_VARIABLES['DB_LOCAL_PORT']
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{IP}:{PORT}/{DB_NAME}'

