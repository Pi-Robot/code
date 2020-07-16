import RPi.GPIO as GPIO
import pin
import control
import time
import sys, pygame
from pygame.locals import *

pygame.init()

pin.load("config1.json")
control.load("config1.json")

motorRight = 0
motorLeft = 0

size = width, height = 600,400
screen = pygame.display.set_mode(size)

while(True):        
    time.sleep(0.2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GPIO.cleanup()
            pygame.display.quit()
            sys.exit()           
        elif event.type == KEYDOWN and event.key == K_ESCAPE:            
            GPIO.cleanup()
            pygame.display.quit()
            sys.exit()            
        elif event.type == KEYDOWN and event.key == K_w:            
            motorRight += 10
            motorLeft += 10
        elif event.type == KEYDOWN and event.key == K_s:            
            motorRight -= 10
            motorLeft -= 10
        elif event.type == KEYDOWN and event.key == K_d:            
            motorRight += 10
            motorLeft -= 10    
        elif event.type == KEYDOWN and event.key == K_a:            
            motorRight -= 10
            motorLeft += 10
        elif event.type == KEYDOWN :            
            motorRight = 0
            motorLeft = 0

    # turn back the wheels to straight direction
    if(motorLeft>motorRight):
        motorLeft-=1
        motorRight+=1
    if(motorLeft<motorRight):
        motorLeft+=1
        motorRight-=1

    # set borders
    if(motorLeft>100):
        motorLeft=100
    if(motorLeft<-100):
        motorLeft=-100
    if(motorRight>100):
        motorRight=100
    if(motorRight<-100):
        motorRight=-100

    # real movement        
    print(motorLeft,motorRight)
    control.move(motorLeft,motorRight)  
   
# reset the GPIOs
GPIO.cleanup()
