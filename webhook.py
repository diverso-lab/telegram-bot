from flask import Flask
from flask import request
from flask import json
from request_handler import handle_request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hook_root():
    if request.headers['CONTENT_TYPE'] == 'application/json':
        event = request.headers.get('X-GitHub-Event')
        json = request.get_json()
        notification = handle_request(event, json)
        print(notification)
        return 'JSON posted'


if __name__ == '__main__':
    app.run(debug=True)
