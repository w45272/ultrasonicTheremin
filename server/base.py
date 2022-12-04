from flask import Flask
from flask_sock import Sock
import time
import RPi.GPIO as GPIO
import theremin

api = Flask(__name__)
sock = Sock(api)

@sock.route('/note')
def note(ws):
    buzzer = GPIO.PWM(triggerPIN, 440) # Set frequency to 1 Khz
    buzzer.start(10)

    try:
        while True:
            dist = theremin.distance()
            # print(dist)
            ws.send(dist)
            buzzer.ChangeFrequency(dist*10)

    except KeyboardInterrupt:
       GPIO.cleanup()
    # for i in range(10):
    #     ws.send(i)
    #     sleep(1)


# @sock.route('/echo')
# def echo(ws):
#     while True:
#         data = ws.receive()
#         ws.send(data)
#
# @api.route('/profile')
# def my_profile():
#     response_body = {
#         "name": "Nagato",
#         "about" :"Hello! I'm a full stack developer that loves python and javascript"
#     }
#
#     return response_body
