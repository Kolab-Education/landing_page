import mailchimp
from app import app


def get_mailchimp_api():
    return mailchimp.Mailchimp(app.config['MAILCHIMP_API_KEY'])
