import pin
import stepper

pin.load("config2.json")
stepper.load("config2.json")

stepper.rel(0,512)
stepper.rel(0,-256)

stepper.abs(0,0)

pin.cleanup()


    
