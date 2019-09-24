#!/usr/bin/env python
#
# Hannah Woody
# Homework 3
# Temp Limits

import Adafruit_BBIO.GPIO as GPIO
import smbus
import time

bus = smbus.SMBus(2)
tmp101_1 = 0x49
tmp101_2 = 0x48

# GPIO pin setup
alert1 = "P8_7"
alert2 = "P8_9"

reset = "P8_8"

GPIO.setup(reset, GPIO.IN)

# Setting up internal pulldown
GPIO.setup(reset, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# T High and T Low setup
bus.write_byte_data(tmp101_1, 3, 28)
bus.write_byte_data(tmp101_1, 2, 25)
bus.write_byte_data(tmp101_2, 3, 28)
bus.write_byte_data(tmp101_2, 2, 25)

def Alarm(alert):
    #temp sensor 1
    if alert == alert1:
        print("Temp Sensor 1 Alert!")
        time.sleep(0.3)
        
    #temp sensor 2
    if alert == alert2:
        print("Temp Sensor 2 Alert!")
        time.sleep(0.3)
        
GPIO.setup(alert1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(alert2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(alert1, GPIO.BOTH, callback=Alarm)
GPIO.add_event_detect(alert2, GPIO.BOTH, callback=Alarm)

while True:
    
    temp1 = bus.read_byte_data(tmp101_1, 0)
    temp2 = bus.read_byte_data(tmp101_2, 0)
    print ("Temp1: " + str(temp1), end=" ")
    print ("Temp2: " + str(temp2), end="\r")
