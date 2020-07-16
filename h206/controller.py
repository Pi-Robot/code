# wheel speed
import RPi.GPIO as GPIO
import pin
import control
import time

pin.load("config1.json")
control.load("config1.json")

lastTime=0
iPart = 0
iFactor = 30
pFactor = 4000
velocity = 0
lastVelocity = 0
lastTime = 0
count=0
setPoint=0.01 # set the desired value here

def controller(setPoint):
    global iPart, ifactor, pFactor, velocity, lastVelocity
    workingPoint = (setPoint / 0.12) * 100 # max speed = 0.12
    if lastVelocity == velocity:
        velocity = 0
    delta = setPoint - velocity
    lastVelocity = velocity
    iPart += iFactor * delta
    if(iPart<0):
        iPart=0
    pPart = pFactor * delta
    left = workingPoint + pPart + iPart
    left=max(min(left,100),0)    
    return left, delta

def counter(channel):
    global lastTime, velocity
    if lastTime != 0:
        delta = (time.time()-lastTime)*1000
        velocity = 1 / delta
    lastTime = time.time()


# setup the event
GPIO.add_event_detect(4, GPIO.BOTH, callback=counter)


i=0
while i<1000:
    time.sleep(0.005)
    left, delta = controller(setPoint) # setpoint
    control.move(left,0)
    count+=1
    if count >100:
        count=0
        print(left, velocity, setPoint, delta, iPart)
    i+=1


GPIO.cleanup()
