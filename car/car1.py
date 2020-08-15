import pin
import control
import time

pin.load("config1.json")
control.load("config1.json")

control.move(80,60)
time.sleep(3)
control.move(-100,90)
time.sleep(3)

# reset the GPIOs
pin.cleanup()
