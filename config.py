import os

class Config(object):
    """
    https://flask.palletsprojects.com/en/1.1.x/config/
    """
    # Flask configuration values
    ENV = os.environ.get('FLASK_ENV')
    DEBUG = os.environ.get('FLASK_DEBUG')
    TESTING = os.environ.get('FLASK_TESTING')
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or os.urandom(16)
    SERVER_NAME = os.environ.get('FLASK_SERVER_NAME')

    # Flask-SQLAlchemy configuration values
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_ECHO = os.environ.get('FLASK_SQLALCHEMY_ECHO')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Stripe
    STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
    STRIPE_SUBSCRIPTION_PLAN_ID = os.environ.get('STRIPE_SUBSCRIPTION_PLAN_ID')
    DOMAIN = os.environ.get('DOMAIN')

class DevelopmentConfig(Config):
    # Flask configuration values
    ENV = 'development'
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    # Flask configuration values
    ENV = 'production'
    DEBUG = False
    TESTING = False
