# load the JSON file and init the data
import json
import pin

motorCount = 6
motor = [ [] for f in range(motorCount)] # contains the class Stepper


class Motor:
    def __init__(self,position):
        self.run = False
        self.start= position
        self.position = position
        self.end = position
        self.factor = 0
        self.dir = 1
        self.outputs = ['','','','']
        self.state = 0 # index of the queue

    # set the names of the motor pins
    def setOutput(self,index,name):
        if index>3 or index<0:
            print("stepper1N index out of range")
            exit        
        self.outputs[index] = name    

    # set the end position    
    def setDestination(self,destination):
        self.start=self.end
        self.end += destination
        print("Star:",self.start," End: ", self.end) # debug        
        self.factor = (self.end-self.start) / 100000        
        if self.factor <0:
            self.dir =-1
        else:
            self.dir = 1
        if self.start != self.end:
            self.run = True
        else:
            self.run = False
            
    # check the dest position and do a single step
    def setPosition(self,pointer):
        if self.run:
            destPosition = self.start + round(self.factor * pointer)
            if self.position != destPosition:
                self.position += self.dir
                self.state += self.dir
                self.state %= 4
                self.step()

    # do a single step
    def step(self):
        queue = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        for i in range(4):        
            pinName=self.outputs[i] # index starts with 0            
            value=queue[self.state][i]            
            pin.Out(pinName,value) # set the output pin

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
 
    for item in items:
        pin = item["name"]
        # store the items by name        
        if((item["stepperID"] or item["stepperID"]==0)\
           and (item["stepper1N"] or item["stepper1N"]==0)):
            ID=item["stepperID"]
            n = item["stepper1N"]            
            try:        
                motor[ID].setOutput(n,pin)
            except:
                # initialize
                motor[ID] = Motor(0) # new class                
                motor[ID].setOutput(n,pin)
                
                
                


    
  
    
   
