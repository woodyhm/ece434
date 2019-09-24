#!/bin/sh
# Tempurature Read and convert to Fahrenheit

#import Adafruit_BBIO.GPIO as GPIO

# GPIO pin setup
#t1 = "P8_7"
#t2 = "P8_9"

#l1 = "P9_27"
#l2 = "P9_30"

#reset = "P8_8"

#temp=`i2cget -y 2 0x48`

temp1=`i2cget -y 2 0x48`
temp2=`i2cget -y 2 0x49`

echo -n "Temp Sensor 1: "
echo $(($temp1))

echo -n "Temp Sensor 2: "
echo $(($temp2))

# Low
i2cset -y -r 2 0x48 0x02 27
i2cset -y -r 2 0x49 0x02 27

# High
i2cset -y -r 2 0x48 0x03 28
i2cset -y -r 2 0x49 0x03 28

#*18/10+32

#i2cget -y 2 0x48 0x2 27


#if []
#then
#    echo -n "Temp Sensor 1: "
#    echo $(($temp1*18/10+32))
#    echo -n "Temp Sensor 2: "
#    echo $(($temp2*18/10+32))
#fi