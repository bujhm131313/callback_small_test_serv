from flask import Flask, request
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/callback_route', methods=['POST'])
def callback():
    data = request.data
    json = request.json

    with open('{}/dump.txt'.format(app.root_path), 'w') as file:
        file.write(str(data))
        file.write(str(json))

    return 'ok'


if __name__ == '__main__':
    app.run()
