#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import picamera

# Constants
ON = True
OFF = False
pin_button = 12
pin_led = 8

# Functions
def snap(name):
	with picamera.PiCamera() as camera:
		camera.resolution = (1024, 768)
		camera.start_preview()
		countDown(3, 1)    # slow blink for 3
		countDown(1, 0.1)  # fast blink for 1
		camera.capture(name)

def getLed():
    return GPIO.input(pin_led)

def getButton():
	return GPIO.input(pin_button)

def setLed(state):
    GPIO.output(pin_led, state)

def toggle():
	setLed(not(getLed()))

def countDown(seconds, interval):
	for n in range(seconds):
		for t in range(int(1/interval)):
			toggle()
			time.sleep(interval)

def setupGPIO():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin_button, GPIO.IN)
    GPIO.setup(pin_led, GPIO.OUT)
    setLed(OFF)

def click():
    snap('pic.png')

# Do the main work of the program
try:
	setupGPIO()
	prev = -1
	while True:
		state = getButton()
		if (0 == prev) and (1 == state) :
			click()
		prev = state
		time.sleep(0.1)
except KeyboardInterrupt:
	print("\nDone")
