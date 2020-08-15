# wheel speed
import pin
import control
import time
import RPi.GPIO as GPIO

pin.load("config1.json")
control.load("config1.json")

lastTime=0
count=0

# define the function
def counter(channel):
    global lastTime, count    
    if(count==0):
        lastTime=int(round(time.time()*1000))
        print(time.time())
    count+=1        
    if(count >= 40):
        delta=int(round(time.time()*1000)) - lastTime
        print(count/delta, count, delta)        
        count=0
    
# setup the event
GPIO.add_event_detect(4, GPIO.BOTH, callback=counter)

control.move(100,0)
time.sleep(5)
pin.cleanup()
