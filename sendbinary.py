import RPi.GPIO as GPIO
from time import sleep
import convert

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(15, GPIO.IN)
GPIO.output(18, True)

bin = convert.generateSignal("test")
waitTime = 2
for letter in bin:
    if(letter == '1'):
        GPIO.output(18, True)
    else:
        GPIO.output(18, False)
    sleep(waitTime)
    
GPIO.cleanup()
    
            
            
        
