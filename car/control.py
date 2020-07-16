# load the JSON file and init the data
import json
import pin 

# store all the items in dict after read json
controlItems = {} 

# open the file
def load(filename):
    try:
        # open
        with open(filename, "r") as file:            
            # read and parse JSON
            items = json.loads(file.read())
    except:
        # if something goes wrong
        print("Error loading",filename)
        exit(0)

    # initialize all pins as
    # right1, right2, rightPower
    # left1, left2, leftPower
    global controlItems
    allowedWords = ["right1","right2","rightPower","left1","left2","leftPower"]
    for item in items:
        pin = item["pin"]
        # store the items by name
        # i.e. controlItems["right1"] =  ...
        if(item["control"]):
            if(not(item["control"] in allowedWords)):
                print("Value not allowed for \"control\":",item["control"])               
                exit(0)
            controlItems[item["control"]] = item;
                    


# turn two motors
def move(left, right):
    global controlItems
    # left side
    if(left>0):
        pin.Out(controlItems["left1"]["name"],1)
        pin.Out(controlItems["left2"]["name"],0)
    else:    
        pin.Out(controlItems["left1"]["name"],0)
        pin.Out(controlItems["left2"]["name"],1)    
    pin.Level(controlItems["leftPower"]["name"],abs(left))
    # right side
    if(right>0):
        pin.Out(controlItems["right1"]["name"],1)
        pin.Out(controlItems["right2"]["name"],0)
    else:    
        pin.Out(controlItems["right1"]["name"],0)
        pin.Out(controlItems["right2"]["name"],1)    
    pin.Level(controlItems["rightPower"]["name"],abs(right))
    
   
