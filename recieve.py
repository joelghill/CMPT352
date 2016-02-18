import RPi.GPIO as GPIO
import time
import convert
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.IN)
message = ""
wait = 0.1
while(1):
	if(GPIO.input(7)):
		character = ""
		time.sleep(wait)
		print("recieving")
		while(1):
			character = character + str( GPIO.input(7))
			if (len(character) == 8 ):
				print(character)
				if (convert.endT() == character):
					message = message + character
					print(message)
					message = convert.parseSignal(message)
					print(message)
					data = open('data.txt','w')
					data.write(message)
					data.close()
					break
				else:
					message = message + character
					character = "" 
			time.sleep(wait)
GPIO.cleanup()
