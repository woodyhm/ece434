#!/usr/bin/env python
#
# Hannah Woody
# Homework 3
# Etch-a-sketch

import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2, eQEP1
import time
import smbus

l_Encoder = RotaryEncoder(eQEP2)
l_Encoder.setAbsolute()
l_Encoder.enable()

r_Encoder = RotaryEncoder(eQEP1)
r_Encoder.setAbsolute()
r_Encoder.enable()

bus = smbus.SMBus(2)
matrix = 0x70

# LED Matrix Setup
bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)

leds  = [0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00]
        
clear=[0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00, 
        0x00, 0x00]
        
# Inital Write to LED Matrix
bus.write_i2c_block_data(matrix, 0, leds)

# GPIO pin setup
b1 = "P8_11"
b2 = "P8_12"
b3 = "P8_17"
b4 = "P8_18"
#reset = "P8_8"

GPIO.setup(b1, GPIO.IN)
GPIO.setup(b2, GPIO.IN)
GPIO.setup(b3, GPIO.IN)
GPIO.setup(b4, GPIO.IN)
#GPIO.setup(reset, GPIO.IN)

GPIO.setup(b1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(reset, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Grid setup
x = 3
y = 3
width = 7
height = 7

# Initalize Encoder Position
r = r_Encoder.position
l = l_Encoder.position
r_updated = r
l_updated = l
    
while True:
    
    r_updated = r_Encoder.position
    l_updated = l_Encoder.position
    
    # x position
    if(r_updated < r):
        x+=1
        if(x > width):
            x = 0
        time.sleep(0.1)
    if(r_updated > r):
        x-=1
        if(x < 0):
            x = width
        time.sleep(0.1)

        # y position
    if(l_updated < l):
        y+=1
        if(y > height):
            y = 0
        time.sleep(0.1)
    if(l_updated > l):
        y-=1
        if(y < 0):
            y = height
        time.sleep(0.1)
    
    #reset button which clears terminal and sets the cursor back to position (3,3)
    if GPIO.input(b1):
        bus.write_i2c_block_data(matrix, 0, clear)
        break
        
    r = r_updated
    l = l_updated
    
    leds[2*x] = leds[2*x]|(0x80>>y)
    bus.write_i2c_block_data(matrix, 0, leds)