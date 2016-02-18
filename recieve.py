import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.IN)
while(1):
	if(GPIO.input(7)):
		while(character != 0x04):
			message = message + GPIO.input(7)
			time.sleep(2)
		

GPIO.cleanup()
