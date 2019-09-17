#!/usr/bin/env python
#
# Hannah Woody
# Homework 2
# Buttons and LEDs

import Adafruit_BBIO.GPIO as GPIO

# GPIO pin setup
b1 = "P8_16"
b2 = "P8_18"
b3 = "P9_23"
b4 = "P8_17"

l1 = "P9_27"
l2 = "P9_30"
l3 = "P9_41"
l4 = "P8_26"

# Setting up inputs and outputs
GPIO.setup(b1, GPIO.IN)
GPIO.setup(b2, GPIO.IN)
GPIO.setup(b3, GPIO.IN)
GPIO.setup(b4, GPIO.IN)

GPIO.setup(l1, GPIO.OUT)
GPIO.setup(l2, GPIO.OUT)
GPIO.setup(l3, GPIO.OUT)
GPIO.setup(l4, GPIO.OUT)

# Setting up internal pulldown
GPIO.setup(b1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while(1):
    if GPIO.input(b1):
        GPIO.output(l1, GPIO.HIGH)
        print("b1 pressed")
    if GPIO.input(b2):
        GPIO.output(l2, GPIO.HIGH)
        print("b2 pressed")
    if GPIO.input(b3):
        GPIO.output(l3, GPIO.HIGH)
        print("b3 pressed")
    if GPIO.input(b4):
        GPIO.output(l4, GPIO.HIGH)
        print("b4 pressed")
    else:
        GPIO.output(l1, GPIO.LOW)
        GPIO.output(l2, GPIO.LOW)
        GPIO.output(l3, GPIO.LOW)
        GPIO.output(l4, GPIO.LOW)
        print("none pressed")