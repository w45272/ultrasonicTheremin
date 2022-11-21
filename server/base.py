from flask import Flask
from flask_sock import Sock

api = Flask(__name__)
sock = Sock(api)


@sock.route('/echo')
def echo(ws):
    while True:
        data = ws.receive()
        ws.send(data)

@api.route('/profile')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body
