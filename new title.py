# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

pygame.init()


size   = [1800, 1000]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("2021 BLUE MARBLE")

font = pygame.font.SysFont('Constantia', 18)

#define colours
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0, 153, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
GRAY = (127,127,127)

#define global variable
clicked = False
counter = 0

font1 = pygame.font.Font('Maplestory Bold.ttf',70)
img1 = font1.render('부루마불 2021',True,BLACK)
marbleimage = pygame.image.load('marble.jpg')
marbleimage =pygame.transform.scale(marbleimage,(500,500))

class button():
		
	#colours for button and text
	button_col = (50, 30, 255)
	hover_col = (75, 225, 255)
	click_col = (50, 150, 255)
	text_col = BLACK
	width = 180
	height = 70

	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text

	def draw_button(self):

		global clicked
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#create pygame Rect object for the button
		button_rect = Rect(self.x, self.y, self.width, self.height)
		
		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(screen, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(screen, self.hover_col, button_rect)
		else:
			pygame.draw.rect(screen, self.button_col, button_rect)
		
		#add shading to button
		pygame.draw.line(screen, WHITE, (self.x, self.y), (self.x + self.width, self.y), 2)
		pygame.draw.line(screen, WHITE, (self.x, self.y), (self.x, self.y + self.height), 2)
		pygame.draw.line(screen, BLACK, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
		pygame.draw.line(screen, BLACK, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

		#add text to button
		text_img = font.render(self.text, True, self.text_col)
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action



casual = button(580, 350, 'CASUAL MODE')
classic = button(580, 450, 'CLASSIC MODE')
hardcore = button(580, 550, 'HARDCORE MODE ')


run = True
while run:
    
    screen.fill(BLUE)
    screen.blit(img1, (470,70))
    screen.blit(marbleimage, (1000, 300))
    if casual.draw_button():
        counter=1
        
    if classic.draw_button():
        counter=2
    if hardcore.draw_button():
        counter=3

  
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False	
    

    pygame.display.update()


pygame.quit()