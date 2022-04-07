from flask import Flask
from flask import request
from flask import json
from request_handler import handle_request
from telegram_bot import send_telegram_notification
app = Flask(__name__)


@app.route('/', methods=['POST'])
def hook_root():
    if request.headers['CONTENT_TYPE'] == 'application/json':
        event = request.headers.get('X-GitHub-Event')
        json = request.get_json()
        notification = handle_request(event, json)
        if notification is not None:
            send_telegram_notification(notification)
        return 'JSON posted'


if __name__ == '__main__':
    app.run()
