#!/usr/bin/env python
#
# Hannah Woody
# Homework 2
# Etch-a-sketch

import Adafruit_BBIO.GPIO as GPIO
import time
import curses
import sys

# GPIO pin setup
b1 = "P8_16"
b2 = "P8_18"
b3 = "P9_23"
b4 = "P8_17"
reset = "P8_8"

l1 = "P9_27"
l2 = "P9_30"
l3 = "P9_41"
l4 = "P8_26"

# Setting up inputs and outputs
GPIO.setup(b1, GPIO.IN)
GPIO.setup(b2, GPIO.IN)
GPIO.setup(b3, GPIO.IN)
GPIO.setup(b4, GPIO.IN)
GPIO.setup(reset, GPIO.IN)

GPIO.setup(l1, GPIO.OUT)
GPIO.setup(l2, GPIO.OUT)
GPIO.setup(l3, GPIO.OUT)
GPIO.setup(l4, GPIO.OUT)

# Setting up internal pulldown
GPIO.setup(b1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(reset, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# setting up cursor
stdscr = curses.initscr()

# This function makes an area defined by the variables row and col to play an Etch-a-sketch game using buttons on the BeagleBone
def main(stdscr):

    curses.curs_set(0)
    
    # row and col define sketching area
    row = 8
    col = 8
    
    # variables used for moving the cursor
    x = 0
    y = 0
    
    while(1):
        #button 1
        if GPIO.input(b1):
            GPIO.output(l1, GPIO.HIGH)
            if x >= (row*2) - 2:
                x = x - 2 
            x = x + 2
            stdscr.addstr(y, x, "X ")
            time.sleep(0.1)
            GPIO.output(l1, GPIO.LOW)
        #button 2
        if GPIO.input(b2):
            GPIO.output(l2, GPIO.HIGH)
            if y <= 0:
                y = y + 1
            y = y - 1
            stdscr.addstr(y, x, "X")
            time.sleep(0.1)
            GPIO.output(l2, GPIO.LOW)
        #button 3
        if GPIO.input(b3):
            GPIO.output(l3, GPIO.HIGH)
            if y >= col-1:
                y = y - 1
            y = y + 1
            stdscr.addstr(y, x, "X")
            time.sleep(0.1)
            GPIO.output(l3, GPIO.LOW)
        #button 4
        if GPIO.input(b4):
            GPIO.output(l4, GPIO.HIGH)
            if x <= 0:
                x = x + 2
            x = x - 2
            stdscr.addstr(y, x, "X ")
            time.sleep(0.1)
            GPIO.output(l4, GPIO.LOW)
        #reset button which clears terminal and sets the cursor back to position (0,0)
        if GPIO.input(reset):
            stdscr.addstr(y, x, "clear")
            stdscr.clear()
            x = 0
            y = 0
            time.sleep(1)
        if GPIO.input(b1) and GPIO.input(b2) and GPIO.input(b4):
            GPIO.output(l1, GPIO.HIGH)
            GPIO.output(l2, GPIO.HIGH)
            GPIO.output(l3, GPIO.HIGH)
            GPIO.output(l4, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(l1, GPIO.LOW)
            GPIO.output(l2, GPIO.LOW)
            GPIO.output(l3, GPIO.LOW)
            GPIO.output(l4, GPIO.LOW)
            sys.exit()
            
        stdscr.refresh()
        time.sleep(0.1)

curses.wrapper(main)

#curses.endwin()    # To close window