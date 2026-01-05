# light bulb
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
greenbulb=5
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

var=0
x=0
y=0
GPIO.setup(greenbulb, GPIO.OUT)
GPIO.output(greenbulb, GPIO.LOW)
p=GPIO.PWM(greenbulb, 15)
p.start(var)
while True:
    clock.tick(10)
    screen.fill((0,0,0))
    show_text(str(var),500,300,colour.white,30)
    increase=pygame.draw.rect(screen,(colour.green),(300,500,100,100))
    p.ChangeDutyCycle(var)
    reduce=pygame.draw.rect(screen,(colour.red),(600,500,100,100))
    

    for event in pygame.event.get():
        if event.type==QUIT:
            p.close()
            pygame.quit()
            exit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            x,y=event.pos
            print(x,y)
            if event.button==1:
                if increase.collidepoint(event.pos):
                    var += 1
                if reduce.collidepoint(event.pos):
                    var=var-1

    pygame.display.update()
