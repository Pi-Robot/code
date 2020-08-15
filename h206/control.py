# load the JSON file and init the data
import json
import pin 

# store all the names in dict after read json
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
    for name, item in items.items():        
        # store the items by name
        # i.e. controlItems["right1"] =  ...
        if "control" in item:
            if(not(item["control"] in allowedWords)):
                print("Value not allowed for \"control\":",item["control"])               
                exit(0)
            controlItems[item["control"]] = name;
                    


# turn two motors
def move(left, right):
    global controlItems
    # left side
    if(left>0):
        pin.Out(controlItems["left1"],1)
        pin.Out(controlItems["left2"],0)
    else:    
        pin.Out(controlItems["left1"],0)
        pin.Out(controlItems["left2"],1)    
    pin.Level(controlItems["leftPower"],min(abs(left),100))
    # right side
    if(right>0):
        pin.Out(controlItems["right1"],1)
        pin.Out(controlItems["right2"],0)
    else:    
        pin.Out(controlItems["right1"],0)
        pin.Out(controlItems["right2"],1)    
    pin.Level(controlItems["rightPower"],min(abs(right),100))
    
   
