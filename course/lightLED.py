# light LED by switch
import pin

# use "pin module" to load and configure all pins
pin.load()

try:
    # endless loop until "Crtl + c"
    while(True):
        # read the status of the switch
        status = pin.In("switch")
        # set the led1 to ON or OFF
        if(status == 0 ):
            pin.Out("led1", 1) # ON
        else:
            pin.Out("led1", 0) # OFF
            
# handle Crtl +c        
except KeyboardInterrupt:   
    print("End")
finally:
    # reset the GPIOs
    pin.cleanup()
    
