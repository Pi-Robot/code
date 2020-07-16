# threading class
import threading
import time


class myThread (threading.Thread):
   def __init__(self, name, counter, delay):
      threading.Thread.__init__(self)      
      self.name = name
      self.counter = counter
      self.delay = delay
   def run(self):
      print ("Start " + self.name)      
      printCount(self.name, self.counter, self.delay)      
      print ("End " + self.name)

def printCount(name, counter, delay):
    while counter:
        print(name+"-Counter: "+str(counter))
        time.sleep(delay)
        counter-=1
        
thread1 = myThread("Big-Thread", 50, 0.25)
thread2 = myThread("Small-Thread", 20, 0.5)

# Start new Threads
thread1.start()
thread2.start()

# test 1
"""
thread1.join()
thread2.join()
"""

#test 2
"""
for i in range(40):
    print("Simple Counter",i)
    time.sleep(0.4)
"""

#test3
"""
while thread1.isAlive():
   time.sleep(0.1)
"""
