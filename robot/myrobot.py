# threading class
import time
import json

import pin
import stepper
import robotthread as rt

pin.load("config1.json")
stepper.load("config1.json")

try:
    # open
    filename = "robot1.json"
    with open(filename, "r") as file:            
        # read and parse JSON        
        settings = json.loads(file.read())
except:
    # if something goes wrong
    print("Error loading",filename)
    exit(0)


for data in settings:
    position = data["position"]
    duration= data["time"]
    for i in range(len(position)):
        # set the destinations
        stepper.motor[i].setDestination(position[i])
    rt.start(stepper,duration)
    while rt.SoL():
        time.sleep(0.1)
        
pin.cleanup()
