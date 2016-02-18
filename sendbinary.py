import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(15, GPIO.IN)
GPIO.output(18, False)

bin = "101010101010101010101010101010"
waitTime = 0.001
for letter in bin:
    if(letter == '1'):
        GPIO.output(18, True)
    else:
        GPIO.output(18, False)
    sleep(waitTime)

            
            
        
