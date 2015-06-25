import pygame, sys
from pygame.locals import *
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Hello World!')
pygame.key.set_repeat(True)
 
BLUE = (  0,   0, 255)
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 120), 40)
sprite1 = pygame.image.load("sprite1.png")
sprite2 = pygame.image.load("sprite2.png")
sprite3 = pygame.image.load("sprite3.png")
sprite4 = pygame.image.load("sprite4.png")

bunny_x = 0
bunny_y = 0
i=0
while True: # main game loop
     DISPLAYSURF.fill((200, 200, 200))
     
     for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit()
             sys.exit()
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print('Forward')
                bunny_y -= 1
            if event.key == pygame.K_s:
                bunny_y += 1
            if event.key == pygame.K_a:
                bunny_x -= 1
            if event.key == pygame.K_d:
                bunny_x += 1
                 
     i = i + 1
     if i <= 100:
         DISPLAYSURF.blit(sprite1, (bunny_x,bunny_y))
     elif i <=200:
         DISPLAYSURF.blit(sprite2, (bunny_x,bunny_y))
     elif i <=300:
         DISPLAYSURF.blit(sprite3, (bunny_x,bunny_y))
     elif i <=400:
         DISPLAYSURF.blit(sprite4, (bunny_x,bunny_y))    
     if i == 400:
         i=0
     #DISPLAYSURF.blit(sprite1, (bunny_x,bunny_y))
     pygame.display.update()

