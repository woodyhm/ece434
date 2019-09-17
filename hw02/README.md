I was able to wire up the buttons with the LEDs and make each LED light up according to a corresponding button. The program to achieve this is called BlinkLED.

I then used an ocsilloscope to measure the output of your gpio pins and answer the following questions:

Questions for Shell:
    
    1. What's the min and max voltage? min=-40mV, max=3.44V
    2. What period is it? period=238ms
    3. How close is it to 100ms? 138ms more than 100ms
    4. Why do they differ? the 100ms does not take into account the sleep time, which is why it is about half.
    5. Run htop and see how much processor you are using. 3.3%
    6. Try different values for the sleep time (2nd argument). What's the shortest period you can get? Make a table of the values you try and the corresponding period and processor usage.
    
        Sleep Time:                 Period:                 Processor Usage:
        0.05                        140ms                   5.4%
        0.01                        57ms                    13.2%
        0.001                       39ms                    20.9%
        0.0001                      36ms                    21.2%
        0.00001                     36ms                    21.7%
        0.000001                    36ms                    22.2%
        
        The shortest period I can get is 36ms.
    
    7. How stable is the period? It stays within a ms and occasionally spikes up to around 70ms
    8. Try launching something like vi. How stable is the period? The period went up to 41ms and became more stable
    9. Try cleaning up togglegpio.sh and removing unneeded lines. Does it impact the period? The period seemed to stay the same.
    10. togglegpio uses bash (first line in file). Try using sh. Is the period shorter? Yes, the period dropped to 26ms.
    11. What's the shortest period you can get? The shortest I can get is 26ms.
    
Questions for Python:
    
    1. What's the min and max voltage? min=-40mV, max=3.40V
    2. What period is it? period=101us
    3. How close is it to 100ms? very close. Only 1ms off.
    4. Why do they differ? they are barely different, so outside effects.
    5. Run htop and see how much processor you are using. 3.3%
    6. Try different values for the sleep time (2nd argument). What's the shortest period you can get? Make a table of the values you try and the corresponding period and processor usage.
    
        Sleep Time:                 Period:                 Processor Usage:
        0.05                        101ms                   3.4%
        0.01                        21ms                    5.2%
        0.001                       3.3ms                   29.9%
        0.0001                      570us                   53.7%
        0.00001                     385us                   90.9%
        
        The shortest period I can get is 385us.
    
    7. How stable is the period? It stays within 0.1 ms.
    8. Try launching something like vi. How stable is the period? The period became less stable
    9. Try cleaning up togglegpio.sh and removing unneeded lines. Does it impact the period? There is nothing to clean up.
    10. togglegpio uses bash (first line in file). Try using sh. Is the period shorter? there is no bash here.
    11. What's the shortest period you can get? The shortest I can get is 385us.
    
Questions for C:
    
    1. What's the min and max voltage? min=-40mV, max=3.40V
    2. What period is it? period=406us
    3. How close is it to 100ms? not close
    4. Why do they differ? because it stays at 400us
    5. Run htop and see how much processor you are using. 36.3%
    6. Try different values for the sleep time (2nd argument). What's the shortest period you can get? Make a table of the values you try and the corresponding period and processor usage.
    
        Sleep Time:                 Period:                 Processor Usage:
        0.05                        404us                   38.5%
        0.01                        405us                   39.9%
        0.001                       406us                   40.0%
        0.0001                      405us                   39.1%
        0.00001                     407us                   41.5%
        0.000001                    406us                   39.9%
        
        The shortest period I can get is 404us.
    
    7. How stable is the period? It stays within 0.1 ms and occasionally spikes up to around 500us
    8. Try launching something like vi. How stable is the period? The period became less stable
    9. Try cleaning up togglegpio.c and removing unneeded lines. The period seemed to stay the same.
    10. togglegpio uses bash (first line in file). there is no bash here.
    11. What's the shortest period you can get? The shortest I can get is 404us.
    
I wrote a program for the Etch-a-sketch game using buttons. I also added another button for reset and to end the program.

    
