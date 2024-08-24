import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'default_secret_key'
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
    SESSION_COOKIE_NAME = 'google-login-session'
    OAUTHLIB_INSECURE_TRANSPORT = True  

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    OAUTHLIB_INSECURE_TRANSPORT = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
