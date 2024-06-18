# /api1/app.py
from flask import Flask, jsonify, request
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

TRIG = 16
ECHO = 18

@app.route('/ultrasonic_dis', methods=['GET'])
def get_user():
    setup()
    try:
        distance = loop()
    except KeyboardInterrupt:
        destroy()
    return jsonify(distance)


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

def distance():
    GPIO.output(TRIG, 0)
    time.sleep(0.2)

    GPIO.output(TRIG, 1)
    time.sleep(0.1)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        a = 0
    time1 = time.time()
    while GPIO.input(ECHO) == 1:
        a = 1
    time2 = time.time()

    during = time2 - time1
    return during * 340 / 2 * 100

def loop():
    while True:
        dis = distance()
        print ('Distance: %.2f' % dis )
        time.sleep(0.1)
        return int(dis)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    app.run(port=5001)

    
