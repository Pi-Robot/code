# first motor test
import pin
import time

# load the configuration from config1.json
pin.load("config1.json")

print("foreward")
pin.Out("in1",1)
pin.Out("in2",0)
pin.Out("ena",1)

time.sleep(3)

print("backward")
pin.Out("in1",0)
pin.Out("in2",1)
pin.Out("ena",1)

time.sleep(3)
pin.Out("ena",0)
print("stop")

# reset the GPIOs
pin.cleanup()
    

