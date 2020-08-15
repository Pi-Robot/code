# load the JSON file and init the data
import json
import RPi.GPIO as GPIO

# BCM Mode (read the real GPIO)
GPIO.setmode(GPIO.BCM)

# store all the items in dict after read json
pinItems = {} 

# open the file
def load(filename):
    try:
        # open
        with open(filename, "r") as file:            
            # read and parse JSON
            items = json.loads(file.read())
    except:
        # if something goes wrong
        print("Error loading config.json")
        exit(0)
        
    # store the items by name
    # i.e. pinItems["switch"] =  ...
    global pinItems
    pinItems = items;
    
    # initialize all pins as
    # in, out or pwm    
    for name, item in items.items():
        pin = item["pin"]       
        if(item["io"] == "in"):
            # configure an input
            GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

        if(item["io"] == "out"):
            # configure an output
            GPIO.setup(pin, GPIO.OUT)

        if(item["io"] == "pwm"):
            # configure pwm
            GPIO.setup(pin, GPIO.OUT)
            pinItems[name]=GPIO.PWM(pin,500)            


# GPIO input    
def In(name):
    global pinItems    
    return GPIO.input(pinItems[name]["pin"])

# GPIO output
def Out(name,state):
    global pinItems
    GPIO.output(pinItems[name]["pin"], state)

#GPIO pwm level
def Level(name,level):
    global pinItems   
    if(level == 0):
        pinItems[name].stop()
    else:
        pinItems[name].start(0)
        pinItems[name].ChangeDutyCycle(level)

def cleanup():
    GPIO.cleanup()
