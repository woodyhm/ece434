The following table is for the memory map portion of the homework

Device Name:           Start Address:         End Address:

External Memory        0x0000_0000            0x1FFF_FFFF
SRAM internal          0x402F_0400            0x402F_FFFF
GPIO0                  0x44E0_7000            0x44E0_7FFF
UART Registers         0x44E0_9000            0x44E0_9FFF
I2C0                   0x44E0_B000            0x44E0_BFFF
UART1                  0x4802_2000            0x4802_2FFF
UART2                  0x4802_4000            0x4802_4FFF
I2C1                   0x4802_A000            0x4802_AFFF
GPIO1                  0x4804_C000            0x4804_CFFF
I2C2                   0x4819_C000            0x4819_CFFF
UART3                  0x481A_6000            0x481A_6FFF
UART4                  0x481A_8000            0x481A_8FFF
UART5                  0x481A_A000            0x481A_AFFF
GPIO2                  0x481A_C000            0X481A_CFFF
GPIO3                  0x481A_E000            0x481A_EFFF
LCD controller         0x4830_E000            0x4830_EFFF
SDRAM                  0X8000_0000            0X8FFF_FFFF

For the GPIO via mmap portion, I wrote the LEDbutton file to turn on two LEDs
controlled by two buttons wired to the board. I could not get this part working
fully even though I compared my code with functional code. I kept getting an
installation error even though I updated and installed everything. Since this
part did not work, I couldn't get the toggle.c file that I wrote to fully work
either.

For the LCD display, I was able to meet all of the functionality requirements,
which included displaying and rotating an image, displaying a text file, and 
displaying a video.

## Prof. Yoder's comments

Did you demo the LCD to me?  I don't have a record of it.

Grade:  7/10
