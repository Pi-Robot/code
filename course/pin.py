# load the JSON file and init the data
import json
import RPi.GPIO as GPIO

# BCM Mode (read the real GPIO)
GPIO.setmode(GPIO.BCM)

# store all the items in dict after read json
pinItems = {} 

# open the file
def load():
    try:
        # open
        with open("config.json", "r") as file:            
            # read and parse JSON
            items = json.loads(file.read())
    except:
        # if something goes wrong
        print("Error loading config.json")
        exit(0)

    # initialize all pins as
    # in, out or pwm
    global pinItems
    for item in items:
        pin = item["pin"]
        # store the items by name
        # i.e. pinItems["switch"] =  ...
        pinItems[item["name"]] = item;
        if(item["io"] == "in"):
            # configure an input
            GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

        if(item["io"] == "out"):
            # configure an output
            GPIO.setup(pin, GPIO.OUT)


# GPIO input    
def In(name):
    global pinItems    
    return GPIO.input(pinItems[name]["pin"])

# GPIO output
def Out(name,state):
    global pinItems
    GPIO.output(pinItems[name]["pin"], state)
   
