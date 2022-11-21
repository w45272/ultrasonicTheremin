from flask import Flask
from flask_sock import Sock
from time import sleep

api = Flask(__name__)
sock = Sock(api)


@sock.route('/note')
def note(ws):
    for i in range(10):
        ws.send(i)
        sleep(1)

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
