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
        file.write('\n\nREQUEST DATA: \n' + str(data) + '\n')
        file.write('\n\nREQUEST JSON: \n' + str(json) + '\n')

    return 'ok'


if __name__ == '__main__':
    app.run()
