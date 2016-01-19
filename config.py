import os


SECRET_KEY = os.urandom(24)
SESSION_TYPE = 'filesystem'
MAILCHIMP_API_KEY = os.environ['MAILCHIMP_API_KEY']
EMAIL_SUBSCRIBER_LIST = os.environ['EMAIL_SUBSCRIBER_LIST']
