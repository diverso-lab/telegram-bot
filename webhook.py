from flask import Flask
from flask import request
from flask import json
from request_handler import handle_request
from telegram_bot import send_telegram_notification
from hmac import HMAC, compare_digest
from hashlib import sha256

import os

app = Flask(__name__)

webhook_secret = os.environ['WEBHOOK_SECRET']
host = os.environ['APP_HOST']


def verify_signature(req):
    received_sign = req.headers.get(
        'X-Hub-Signature-256').split('sha256=')[-1].strip()
    secret = webhook_secret.encode()
    expected_sign = HMAC(key=secret, msg=req.data,
                         digestmod=sha256).hexdigest()
    return compare_digest(received_sign, expected_sign)


@app.route('/', methods=['POST'])
def hook_root():
    if request.headers['CONTENT_TYPE'] == 'application/json':
        assert(verify_signature(request))
        event = request.headers.get('X-GitHub-Event')
        json = request.get_json()
        notification = handle_request(event, json)
        if notification is not None:
            send_telegram_notification(notification)
        return 'JSON posted'


if __name__ == '__main__':
    app.run(host=host)
