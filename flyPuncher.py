import pygame, sys, random
from pygame.locals import *

#Initializations
pygame.init()
mainClock = pygame.time.Clock()
basicFont = pygame.font.SysFont(None, 48)

#Set up window
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Fly Puncher')

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#Win Message
text = basicFont.render('Win!', True, WHITE, BLACK)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

#Player Character
player = pygame.Rect(300, 400, 50, 50)
playerImage = pygame.image.load('fist.png')
playerSizedImage = pygame.transform.scale(playerImage, (70, 70))
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
swatFly = False
MOVESPEED = 10

#fly enemy
fly = pygame.Rect(320, 240, 25, 25)
flyImage = pygame.image.load('fly1.png')
flySizedImage = pygame.transform.scale(flyImage, (40, 40))
flys = [fly]

#Game Loop

#Control input
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_LEFT or event.key == K_a:
				moveRight = False
				moveLeft = True
			if event.key == K_RIGHT or event.key == K_d:
				moveLeft = False 
				moveRight = True 
			if event.key == K_UP or event.key == K_w:
				moveDown = False 
				moveUp = True
			if event.key == K_DOWN or event.key == K_s:
				moveUp = False
				moveDown = True
			if event.key == K_z:
				swatFly = True
		if event.type == KEYUP:
			if event.key == K_ESCAPE:
				pygame.quit()
			if event.key == K_LEFT or event.key == K_a:
				moveLeft = False
			if event.key == K_RIGHT or event.key == K_d:
				moveRight = False
			if event.key == K_UP or event.key == K_w:
				moveUp = False
			if event.key == K_DOWN or event.key == K_s:
				moveDown = False
			if event.key == K_z:
				swatFly = False
	
	#Move Player
	if moveDown and player.bottom < WINDOWHEIGHT:
		player.top += MOVESPEED
	if moveUp and player.top > 0: 
		player.top -= MOVESPEED
	if moveLeft and player.left > 0:
		player.left -= MOVESPEED
	if moveRight and player.right < WINDOWWIDTH:
		player.right += MOVESPEED

	#fill background
	windowSurface.fill(WHITE)

	#Kill fly
	for fly in flys[:]:
		if player.colliderect(fly):
			if swatFly == True:
				flys.remove(fly)
				windowSurface.blit(text, textRect)

	#Draw fly
	for i in range(len(flys)):
		windowSurface.blit(flySizedImage, fly)

	#Draw Player
	windowSurface.blit(playerSizedImage, player)

	#Draw screen
	pygame.display.update()
	mainClock.tick(40)
