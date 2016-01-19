import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(24)


class ProductionConfig(Config):
    DEBUG = False
    MAILCHIMP_API_KEY = os.environ['MAILCHIMP_API_KEY']
    EMAIL_SUBSCRIBER_LIST = os.environ['EMAIL_SUBSCRIBER_LIST']


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    MAILCHIMP_API_KEY = os.environ['MAILCHIMP_API_KEY']
    EMAIL_SUBSCRIBER_LIST = os.environ['EMAIL_SUBSCRIBER_LIST']


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    MAILCHIMP_API_KEY = os.environ['MAILCHIMP_API_KEY']
    EMAIL_SUBSCRIBER_LIST = os.environ['EMAIL_SUBSCRIBER_LIST']


class TestingConfig(Config):
    TESTING = True
