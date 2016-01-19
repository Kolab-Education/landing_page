from flask import (Flask, render_template,
                   request, json)
from utils import get_mailchimp_api
from app import app


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    try:
        _email = request.form['inputEmail']
        chimp = get_mailchimp_api()
        test = chimp.helper.ping()
        subs = chimp.lists.subscribe(app.config['EMAIL_SUBSCRIBER_LIST'],
                                     {'email': _email})
        return json.dumps({'message': 'User created successfully !'})
    except Exception as e:
        return json.dumps({'error': str(e)})
