#!/usr/bin/env python

# Copyright 2014 the original author or authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# https://github.com/coderdojobelfast/pi.git

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

