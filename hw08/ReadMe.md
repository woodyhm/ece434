2.6 Blinking an LED
    I clones the PRUCookbook, configured the pins, and make the usr3 LED bink 
    by using the make command. make start starts running the code and make stop
    stops it. See table with results from plot: scope_2.6 summarized below.
    
    
5.3 PWM Generator
    I ran pwm1 and switched the GPIO pin to P9_31. I set the delay for the one 
    to 1 and the delay for off to be 0, which made the waveform symmetric and 
    at 50MHz. See table with results from plot: scope_5.3 summarized below.


5.4 Controlling the PWM Frequency
    I ran pwm4. My waveform only shows P9_31 and P9_29 because there are only 
    two channels on the oscilloscopes in the classroom. The highest frequency
    I could get with the two channels is 327 kHz. I ran the pwm-test.c file, 
    but I had issues targeting the file. See table with results from plot: 
    scope_5.4 summarized below.


5.9 Reading the Input at Regular Intervals
    I used the input_setup.sh file to set the taget and configure the pins. I 
    used a button for input and pressed it as fast as I could. This resulted in 
    a speed of 5.21 Hz. See table with results from plot: scope_5.9 summarized
    below.


5.10 Analog Wave Generator
    I ran the setup to target the file sine1.c. I could not record the frequency 
    because the waveform was bad and had no edges. See table with results from 
    plot: scope_5.10 summarized below.


Table

Section     |  Speed (frequency) |   Jitter?     |   Stable?    |   Scope Filename | Standard Deviation
------------|--------------------|---------------|--------------|------------------|---------------------
2.6         |   12.5 MHz         |  Yes          |  Yes         |   scope_2.6      |  -
5.3         |   50   MHz         |  Yes          |  Yes         |   scope_5.3      | 18.3
5.4         |   327  kHz         |  Yes          |  Yes         |   scope_5.4      |  -
5.9         |   5.21 Hz          |  No           |  Yes         |   scope_5.9      | 1.14
5.10        |   No Edges         |  Yes          |  No          |   scope_5.10     |  -

