import pygame
import time
import random
# creating class for snake object
class Snake:
	def __init__(self):
		self.x = 30
		self.y = 10
		self.body = [[30,10],[20,10],[10,10]]
		self.position = 3
	def getbody(self):
		return self.body
# creating class for apple object
class rectangle:
	def __init__(self,color,x,y,w,h):
		self.color = color
		self.rec_x = x
		self.rec_y = y
		self.rec_width = w
		self.rec_height = h
		self.vis = True
	def display(self,s = None):
		if s is  None:
			if self.vis == True:
				pygame.draw.rect(gameDisplay,self.color,[self.rec_x,self.rec_y,self.rec_width,self.rec_height])
			else:
				pygame.draw.rect(gameDisplay,white,[self.rec_x,self.rec_y,self.rec_width,self.rec_height])
		pygame.time.delay(100)
		self.vis = not self.vis
count = 0			# Denotes the score
black = (0,0,0)
red = (255,0,0)
light_red = (155,0,0)
yellow = (255,255,0)
green = (0,255,0)
light_green = (0,155,0)
white = (255,255,255)
# Renders modified text
def text_objects(text,font):
	textSurface = font.render(text,True,black)
	return textSurface,textSurface.get_rect()
# function to create button
def button(msg,x,y,width,height,ic,ac,action = None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	print(click)
	if x+width > mouse[0]>x and y+height>mouse[1]>y:
			pygame.draw.rect(gameDisplay,ic,[x,y,width,height])
			if click[0] == 1 and action !=None:
				action()		
	else:
		pygame.draw.rect(gameDisplay,ac,[x,y,width,height])
	#for text within the botton
	smallText = pygame.font.Font('freesansbold.ttf',20)
	TextSurf,TextRect = text_objects(msg,smallText)
	TextRect.center = ((x+(width/2)),(y+(height/2)))
	gameDisplay.blit(TextSurf,TextRect)
# The exit function
def exit():
	pygame.quit()
	quit()
# The intro layer in the game
def intro():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.fill(white)
		largeText = pygame.font.Font('freesansbold.ttf',75)
		TextSurf,TextRect = text_objects("The Snake Game",largeText)
		TextRect.center = ((display_width/2),(display_height/4))
		gameDisplay.blit(TextSurf,TextRect)
		button("start!",150,250,100,50,green,light_green,game_loop)
		button("Quit",475,250,100,50,red,light_red,exit)
		pygame.display.update()		
		clock.tick(15)
#creating the window for the game
pygame.init()
display_width = 800
display_height = 400
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Snake_Game")
clock = pygame.time.Clock()
#displays the score in the game
def score():
	font = pygame.font.SysFont(None, 25)
	text = font.render("score: "+str(count), True, black)
	gameDisplay.blit(text,(0,0))
#controls every movement pattern of the snake
def move(flag,snake,apple):
	if flag == 1:		#for moving up
		if snake.position == 2: 
			if snake.x <10:
				snake.x +=10
			else:
				snake.x -=10
			snake.body.insert(0,(snake.x,snake.y))
			if collision(snake,apple) == False: 
				snake.body.pop()
		snake.y -= 10
		snake.position = 1
	elif flag == 2:		#for moving down
		if snake.position == 1:
			if snake.x <10:
				snake.x +=10
			else:
				snake.x -=10
			snake.body.insert(0,(snake.x,snake.y))
			if collision(snake,apple) == False: 
				snake.body.pop()
		snake.y += 10
		snake.position = 2
	elif flag == 3:		#for moving right
		if snake.position == 4:
			if snake.y <10:
				snake.y +=10
			else:
				snake.y -=10
			snake.body.insert(0,(snake.x,snake.y))
			if collision(snake,apple) == False: 
				snake.body.pop()
		snake.x += 10
		snake.position = 3
	elif flag == 4:		#for moving left
		if snake.position == 3:
			if snake.y <10:
				snake.y +=10
			else:
				snake.y -=10
			snake.body.insert(0,(snake.x,snake.y))
			if collision(snake,apple) == False: 
				snake.body.pop()
		snake.x -= 10
		snake.position = 4
	#for controlling movement beyond walls
	if snake.x <0:
		snake.x = display_width
	elif snake.x >= display_width:
		snake.x = 0
	if snake.y <0:
		snake.y = display_height
	elif snake.y >= display_height:
		snake.y = 0	
	if(snake.x != snake.body[0][0] or snake.y != snake.body[0][1]):
		snake.body.insert(0,(snake.x,snake.y))
		if collision(snake,apple) == False: 
			snake.body.pop()
#function for detecting snake collision
def snake_coll(snake):
	c = 0
	for pos in snake.getbody():
		if snake.body[0][0] == pos[0] and snake.body[0][1] == pos[1]:
			c = c + 1
		if(c == 2):
			return True
	return False
#the gameover window
def suicide():
	global count	
	largeText = pygame.font.Font('freesansbold.ttf',55)
	TextSurf,TextRect = text_objects("You Got yourself killed!!",largeText)
	TextRect.center = ((display_width/2),(display_height/4))
	gameDisplay.blit(TextSurf,TextRect)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		button("Play Again",150,250,125,50,green,light_green,game_loop)
		button("Quit",500,250,100,50,red,light_red,exit)
		pygame.display.update()
		clock.tick(60)
#for checking all kinds of collision
def collision(snake,apple):
	global count
	if snake.x == apple.rec_x and snake.y == apple.rec_y:
		count +=5
		apple.rec_x = 10 * random.randrange(0,(display_width-apple.rec_width)/10)
		apple.rec_y = 10 * random.randrange(0,(display_height-apple.rec_height)/10) 
		return True
	elif snake_coll(snake) == True: 
		suicide()
		return False 
	else:
		return False
#The main game loop
def game_loop():
	global count
	count = 0	#for score
	flag = 0	#determines the direction of the snake
	snake  = Snake()
	apple = rectangle(red,50,10,10,10)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					flag = 1
				elif event.key == pygame.K_DOWN:
					flag = 2
				elif event.key == pygame.K_RIGHT:
					flag = 3
				elif event.key == pygame.K_LEFT:
					flag = 4	
		gameDisplay.fill(white)
		score()
		move(flag,snake,apple)
		for pos in snake.getbody():
			pygame.draw.rect(gameDisplay,yellow,pygame.Rect(pos[0],pos[1],10,10))
		apple.display()
		collision(snake,apple)
		pygame.display.update()
		clock.tick(120)
#Starting the game
intro()
