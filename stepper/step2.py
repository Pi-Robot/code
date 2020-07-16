import pin
import stepper
import RPi.GPIO as GPIO

pin.load("config2.json")
stepper.load("config2.json")

stepper.rel(1,512)
stepper.rel(1,-256)

stepper.abs(1,0)

GPIO.cleanup()


    
