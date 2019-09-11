# Hannah Woody
# Etch-A-Sketch
#
# This program requires pygame
# To install pygame write the following instructions in the terminal window
#
# $host sudo apt python3-pip
# $pip3 install pygame
#
# This program emulates an Etch-A-Sketch game

import pygame, sys
from pygame.locals import *

#initializes pygame
pygame.init()

#sets screen display and size
screen = pygame.display.set_mode((1000,1000))
screen.fill((255,100,100))

#initializes x and y position
x = 500
y = 500

#game timer
clock = pygame.time.Clock()

while 1:
	#refresh rate
	clock.tick(50)
	#draws while lines
	pygame.draw.circle(screen, (255,0,255), (x,y),5)	
	pygame.display.update()

	#assigns actions to key presses
	key=pygame.key.get_pressed()
	if key[pygame.K_RIGHT]:x+=1
	if key[pygame.K_LEFT]:x-=1
	if key[pygame.K_UP]:y-=1
	if key[pygame.K_DOWN]:y+=1

	#sets up quit and reset protocol
	for event in pygame.event.get():
		if event.type == KEYDOWN and event.key == K_ESCAPE:
			sys.exit()
		elif event.type == KEYDOWN and event.key == K_SPACE:
			screen.fill((255,100,100))

