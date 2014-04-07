#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import *

ON = True
OFF = False
pin_button = 12
pin_led = 8
led_state = None

def setLight(state):
    GPIO.output(pin_led, state)
    global led_state
    led_state = state

def setup() :
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_button, GPIO.IN)
    GPIO.setup(pin_led, GPIO.OUT)
    setLight(OFF)

def toggle() :
    setLight(not(led_state))



setup()
prev = -1

while True:
    state = GPIO.input(pin_button)
    if (0 == prev) and (1 == state) :
        toggle()
    prev = state
    sleep(0.1)

