#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import *
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
led_pin = 8
GPIO.setup(led_pin, GPIO.OUT)
while True:
    GPIO.output(led_pin, True)
    sleep(0.5)
    GPIO.output(led_pin, False)
    sleep(0.5)
