# control up to 6 Motors
import threading
import time

global thread1

class RobotThread (threading.Thread):
    def __init__(self, name, stepper, delta):
        threading.Thread.__init__(self)      
        self.name = name           
        self.delta = delta
        self.stepper = stepper
    def run(self):
        print ("Start " + self.name)      
        self.setRobotPosition(self.delta)      
        print ("End " + self.name)

    def setRobotPosition(self, delta):
        pointer=0
        while pointer < 100000:        
            time.sleep(0.002)
            pointer += delta        
            for i in range(6):
                if self.stepper.motor[i]:               
                    self.stepper.motor[i].setPosition(pointer)


def start(stepper,time):
    delta=(0.002*100000)/time    
    # start all motors with a way > 0
    global thread1
    thread1 = RobotThread("Robot-Thread", stepper, delta)
    thread1.start()

# sign of life
def SoL():
    global thread1
    return thread1.isAlive()
