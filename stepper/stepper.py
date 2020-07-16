# load the JSON file and init the data
import json
import pin
import time

stepperCount = 6 # max number of steppers
stepper = [[] for f in range(stepperCount)] # contains the names of the pins
state = [ [] for f in range(stepperCount)]
position = [ [] for f in range(stepperCount)]

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
  
    global stepper
    global state
    global position
        
    for item in items:
        pin = item["name"]
        # store the items by name        
        if(item["stepperID"] and item["stepper1N"]):
            ID=item["stepperID"]
            n = item["stepper1N"]            
            try:        
                stepper[ID][n]=pin
            except:
                # initialize               
                stepper[ID]=[ [] for f in range(5)]
                stepper[ID][n]=pin
                state[ID]=0 # initial state
                position[ID]=0 # initial position                

# turn relative
def rel(ID,counts):
    global stepper
    global state
    global position
    destination = position[ID] + counts
    queue = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]] 
    while(position[ID] != destination):
        for i in range(0,4):            
            pinName=stepper[ID][i+1] # index starts with 1             
            value=queue[state[ID]][i]            
            pin.Out(pinName,value)
        time.sleep(0.005)        
        if(counts>0):
            position[ID] += 1
            state[ID] += 1
        else:
            position[ID] -= 1
            state[ID] -= 1
        state[ID] %= 4 # modulo operator 4 --> 0, 5 --> 1, ...
        

# turn absolute
def abs(ID, dest):
    counts = dest - position[ID]
    rel(ID,counts)
    
  
    
   
