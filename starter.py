# Template for Starting Pygame code

import pygame
import colour
import random
import time
pygame.init()
screen=pygame.display.set_mode((1900,1000))
from pygame.locals import QUIT
pygame.display.set_caption('Python 101')
clock=pygame.time.Clock()

def show_text(msg, x, y, colorcode, size):
    fontobj= pygame.font.SysFont('freesans', size)
    msgobj = fontobj.render(msg,False,colorcode)
    screen.blit(msgobj,(x, y))

var1=False
var2=False

while True:
    clock.tick(10)
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(colour.green),(0,0,50,100))
    pygame.draw.circle(screen,(colour.blue),(1875,25),25,25)
    pygame.draw.polygon(screen,(colour.red),((1950,900),(1875,1000),(1850,1000)),67)
    pygame.draw.line(screen,(colour.purple),(0,900),(100,1000),15)

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()

        show_text('hi',300,300,colour.green,30)

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
    pygame.display.update()