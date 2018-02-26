from __future__ import division
import pygame
import math
import random
import time

pygame.init()
width = 800
height = 600
size = (width,height)
fps = 120

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

font = pygame.font.Font('fonts/cargo.ttf',40)
score = pygame.font.Font('fonts/cargo.ttf',30)

background = pygame.image.load("images/roadway.jpg")
backrect = background.get_rect()
#author: Crack.com(bart) -> http://opengameart.org/content/golgotha-textures-tunnelroadjpg

carimg = pygame.image.load("images/car.png")
#author: shekh_tuhin -> http://opengameart.org/content/red-car-top-down
car_width = 49

truckimg = pygame.transform.scale(pygame.image.load("images/pickup.png"),(70,145))
#author: TRBRY -> http://opengameart.org/content/car-pickup

tires = pygame.mixer.Sound("sounds/tires_skid.ogg")
tires.set_volume(1)
#author: Mike Koenig (Soundbible) -> http://opengameart.org/content/car-tire-skid-squealing

crash = pygame.mixer.Sound("sounds/crash.ogg")
crash.set_volume(2)
#author: qubodup -> http://opengameart.org/content/crash-collision

countdown1 = pygame.mixer.Sound("sounds/countdown1.ogg")
countdown1.set_volume(1)
countdown1.play()

time.sleep(1)

countdown1 = pygame.mixer.Sound("sounds/countdown1.ogg")
countdown1.set_volume(1)
countdown1.play()

time.sleep(1)

countdown2 = pygame.mixer.Sound("sounds/countdown2.ogg")
countdown2.set_volume(1)
countdown2.play()
#author: Destructavator -> http://opengameart.org/content/countdown

time.sleep(1)

soundtrack = pygame.mixer.Sound("sounds/soundtrack.ogg")
soundtrack.set_volume(0.5)
soundtrack.play(-1)
#author: Dan Knoflicek -> http://opengameart.org/content/steppin-up

def avoided(count):
	scoreFont = score.render("Score: %d" % count, True, (0,0,0))
	screen.blit(scoreFont, (50,570))

def truck(truck_x,truck_y):
	screen.blit(truckimg,(truck_x,truck_y))

def car(x,y):
	screen.blit(carimg,(x,y))

def message2(x):
	messageFont2 = font.render("You hit a truck!", True, (0,0,0))
	rect = messageFont2.get_rect()
	rect.center = ((width//2),(height//2))
	screen.blit(messageFont2, rect)
	
	pygame.display.update()
	
	time.sleep(3)
	
	playing()	
	
def message(x):
	messageFont = font.render("You went off the road!", True, (0,0,0))
	rect = messageFont.get_rect()
	rect.center = ((width//2),(height//2))
	screen.blit(messageFont, rect)
	
	pygame.display.update()
	
	time.sleep(3)
	
	playing()	
	
def crashed2():
	message2("You hit a truck!")

def crashed():
	message("You went off the road!")
	
def playing():
	x = 351
	y = 480 	

	xChange = 0
	
	truck_x = random.randrange(50,770)
	truck_y = -500
	truck_speed = 2
	truck_height = 145
	truck_width = 70

	score = 0
	
	while True:
		
		clock.tick(fps)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					xChange = -6
				if event.key == pygame.K_RIGHT:
					xChange = 6
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					xChange = 0
					
		x += xChange
		
		screen.blit(background, backrect)
		
		truck(truck_x,truck_y)
		truck_y += truck_speed
		
		car(x,y)
		
		avoided(score)
		
		#crash detection if the car goes off the road
		if x > (width - 87) or x < 35:
			tires.play()
			crash.play()
			crashed()
		
		#starting the truck along random coordinates
		if truck_y > height:
			truck_y =- 145
			truck_x = random.randrange(50,770)
			
			score += 1 #increase the score +1 for every truck is avoided
			truck_speed += 0.2 #increase the speed by 0.2 for every truck passed
		
		#collision detection for hitting the truck
		if y < truck_y + 145:
			
			if x > truck_x and x < truck_x + truck_width or x + car_width > truck_x and x + car_width < truck_x + truck_width:
				crash.play()
				crashed2()
		
		pygame.display.flip()
	
playing()
