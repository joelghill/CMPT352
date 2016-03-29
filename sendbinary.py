import RPi.GPIO as GPIO
from time import sleep
import convert

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(15, GPIO.IN)
#GPIO.output(18, True)

bin = convert.generateSignal("Hello World!")
waitTime = 0.1
for letter in bin:
    if(letter == '1'):
        GPIO.output(18, True)
    else:
        GPIO.output(18, False)
    sleep(waitTime)

GPIO.output(18, False)
GPIO.cleanup()




