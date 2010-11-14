import pygame, sys, time, random
from pygame.locals import *
# set up pygame


pygame.init()
mainClock = pygame.time.Clock()

# set up the window
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Ballon eating needles')
TEXTCOLOR = (255, 255, 255)
	
def terminate():
	pygame.quit()
	sys.exit()

def waitForPlayerToPressKey():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE: # pressing escape quits
					terminate()
				return





# set up the colors
GRAY = (128, 128, 128)

#define font
font = pygame.font.SysFont(None, 48)

#defining drawtext function:
def drawText(text, font, surface, x, y):
	textobj = font.render(text, 1, TEXTCOLOR)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y)
	surface.blit(textobj, textrect)

# show the "Start" screen
drawText('Balloons eating Needles', font, windowSurface, (WINDOWWIDTH / 9),(WINDOWHEIGHT / 5))
drawText('Press a key to start.', font, windowSurface,(WINDOWWIDTH / 5)-30, (WINDOWHEIGHT / 5) + 50)
pygame.display.update()
waitForPlayerToPressKey()

topScore=0
time=0

while True:
  	# set up the block data structure
  	player = pygame.Rect(300, 100, 40, 40)
  	playerImage = pygame.image.load('player.png')
  	playerStretchedImage = pygame.transform.scale(playerImage,(40, 40))
  	foodImage = pygame.image.load('cherry.png')
  	foods = []
	score =0
	Timelimit=60000

	for i in range(20):
		foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH- 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))

	foodCounter = 0
	NEWFOOD = 40

	# set up keyboard variables
	moveLeft = False
	moveRight = False
	moveUp = False
	moveDown = False

	MOVESPEED = 6
	

	# run the game loop
	while True:
		# check for the QUIT event
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if event.type == KEYDOWN:
				# change the keyboard variables
			        if event.key == K_LEFT or event.key == ord('a'):
	                		moveRight = False
        	        		moveLeft = True
			        if event.key == K_RIGHT or event.key == ord('d'):
		        	        moveLeft = False
		                	moveRight = True
			        if event.key == K_UP or event.key == ord('w'):
			                moveDown = False
			                moveUp = True
		        	if event.key == K_DOWN or event.key == ord('s'):
		                	moveUp = False
			                moveDown = True

			if event.type == KEYUP:
			        if event.key == K_ESCAPE:
               				pygame.quit()
        		        	sys.exit()
			        if event.key == K_LEFT or event.key == ord('a'):
			                moveLeft = False
			        if event.key == K_RIGHT or event.key == ord('d'):
		        	        moveRight = False
			        if event.key == K_UP or event.key == ord('w'):
			                moveUp = False
			        if event.key == K_DOWN or event.key == ord('s'):
		        	        moveDown = False
			        if event.key == ord('x'):
			                player.top = random.randint(0,WINDOWHEIGHT - player.height)
					player.left = random.randint(0,WINDOWWIDTH - player.width)
	
			if event.type == MOUSEBUTTONUP:
				foods.append(pygame.Rect(event.pos[0] - 10,event.pos[1] - 10, 20, 20))
		foodCounter += 1
		if foodCounter >= NEWFOOD:
			# add new food
			foodCounter = 0
			foods.append(pygame.Rect(random.randint(0,WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20),20, 20))
		# draw the black background onto the surface
		windowSurface.fill(GRAY)
		# move the player
		if moveDown and player.bottom < WINDOWHEIGHT:
			player.top += MOVESPEED
		if moveUp and player.top > 0:
			player.top -= MOVESPEED
		if moveLeft and player.left > 0:
			player.left -= MOVESPEED
		if moveRight and player.right < WINDOWWIDTH:
			player.right += MOVESPEED
	
	
		# draw the block onto the surface
		windowSurface.blit(playerStretchedImage, player)

		# check if the block has intersected with any foodsquares.
		for food in foods[:]:
			if player.colliderect(food):
				foods.remove(food)
				score+=1
				player = pygame.Rect(player.left, player.top,player.width + 2, player.height + 2)
				playerStretchedImage = pygame.transform.scale(playerImage, (player.width, player.height))
		
			
		time=(pygame.time.get_ticks())-time
		drawText('Time: %s' % (time), font,windowSurface, 30, 0)


		# draw the food
		for food in foods:
			windowSurface.blit(foodImage, food)
		# draw the window onto the screen
		pygame.display.update()

		#bursting of ballon
		if time>Timelimit:
			if score>topScore:
        			player = pygame.Rect(player.left,player.top,player.width+2,player.height+2)
        			playerImage = pygame.image.load('player1.png')
				windowSurface.blit(playerImage,player)
				pygame.display.update()
				mainClock.tick(40)
			break
		mainClock.tick(40)

        #windowSurface.fill(BLACK)


	if score > topScore:
                topScore = score # set new top score

	drawText('Topscore: %s' % (topScore), font,windowSurface, (WINDOWWIDTH/2), 0)

	

        # show the "Start" screen
        drawText('Balloons eating Needles', font, windowSurface, (WINDOWWIDTH / 9),(WINDOWHEIGHT / 5))
	drawText('Press a key to start.', font, windowSurface,(WINDOWWIDTH / 5)-30, (WINDOWHEIGHT / 5) + 50)
	pygame.display.update()
	waitForPlayerToPressKey()

