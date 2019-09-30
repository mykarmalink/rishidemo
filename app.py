#!flask/bin/python
import json

from flask import Flask, Response

from demo.flaskrun import flaskrun

application = Flask(__name__)


@application.route('/', methods=['GET'])
def get_root():
    return Response(json.dumps(
        dict(Output='Hello from rishi')),
        mimetype='application/json', status=200)


if __name__ == '__main__':
    flaskrun(application)
