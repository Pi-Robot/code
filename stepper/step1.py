import pin
import time
import RPi.GPIO as GPIO

pin.load("config1.json")

queue = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
pinName = ["1N1","1N2","1N3","1N4"]
state = 0
position = 0 # actual position
destinationCount = 1024

# repeat until position reached
while(position < destinationCount):
    # set all four pins
    for i in range(0,4):
        pin.Out(pinName[i],queue[state][i])
    time.sleep(0.005)
    state+=1
    if(state>3):
        state = 0
    position+=1

GPIO.cleanup()


    
