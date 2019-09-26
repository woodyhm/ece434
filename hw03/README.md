I was able to read the two temperature sensors and get the alert pin working.
when the temperature exceeded 28 degrees C or fell below 25 degrees C, a message
would print saying that a specific temp sensor has an alert.

My etch-a-sketch works with the 8x8 led matrix and the rotary encoders. I ran into
a weird problem where my code wouldn't work once I took out the buttons so I could
only make it work when I set up all of the buttons. I hope it is not a problem 
for future projects.

These were the pins I used for the rotary encoders:

# eQEP 1
config-pin P8_33 qep
config-pin P8_35 qep

# eQEP 2
config-pin P8_41 qep
config-pin P8_42 qep

## Prof. Yoder's comments

Looks good.  

Grade:  10/10