#!/usr/bin/env python
# toggle gpio script in python

import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_12", GPIO.OUT)
sleeptime = 0.00001

state = 0
while(1):
    if state == 0:
        GPIO.output("P9_12", GPIO.HIGH)
        state = 1
        time.sleep(sleeptime)
    else:
        GPIO.output("P9_12", GPIO.LOW)
        state = 0
        time.sleep(sleeptime)