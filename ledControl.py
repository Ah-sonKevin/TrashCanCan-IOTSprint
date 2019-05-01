import RPi.GPIO as GPIO
import time


class LedController:
    endLedPin = 14
    
    def __init__(self):
        self.endLedPin = 14
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.endLedPin,GPIO.OUT)


    def endLed(self):
        print('Turn On Led')
        GPIO.output(self.endLedPin,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(self.endLedPin,GPIO.HIGH)
        print('Turn off led')
