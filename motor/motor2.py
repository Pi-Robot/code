# pwm motor test
import pin
import time

# load the configuration from config2.json
pin.load("config2.json")

print("foreward")
pin.Out("in1",1)
pin.Out("in2",0)
pin.Level("ena",50)

time.sleep(3)

print("backward")
pin.Out("in1",0)
pin.Out("in2",1)
pin.Level("ena",80)

time.sleep(3)

pin.Level("ena",0)
print("stop")

# reset the GPIOs
pin.cleanup()
    

