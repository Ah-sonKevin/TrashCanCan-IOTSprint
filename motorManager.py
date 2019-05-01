import wiringpi
import time
import sys


#Pulse empirically chosen
pulseClockwise = 50  
pulseCounterClockwise = 250
delayFullTurn = 0.65 #empirically chosen
    

sortPin = 18
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(sortPin,wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
#  PWM Frequency in Hz = 19,200,000 Hz / pwmClock / pwmRange  
#Clock and range for a frequency of 50Hz
wiringpi.pwmSetClock(200)
wiringpi.pwmSetRange(1920)

def rotateClockwise(delay):
    wiringpi.pwmWrite(sortPin,pulseClockwise)
    time.sleep(delay)
    wiringpi.pwmWrite(sortPin,0)

def rotateCounterClockwise(delay):
    wiringpi.pwmWrite(sortPin,pulseCounterClockwise)
    time.sleep(delay)
    wiringpi.pwmWrite(sortPin,0)
        
def firstTrash():
    print('first trash')
    rotateClockwise(delayFullTurn*2/3)
    time.sleep(2)
    rotateCounterClockwise(delayFullTurn *2/3)
    
def secondTrash():
    print('second trash')
    rotateCounterClockwise(delayFullTurn*2/3)
    time.sleep(2)
    rotateClockwise(delayFullTurn*2/3)

if(len(sys.argv)>1):
    if( '--left' in sys.argv):
        secondTrash()
    elif ('--right' in sys.argv):
        firstTrash()
else:
    secondTrash()
