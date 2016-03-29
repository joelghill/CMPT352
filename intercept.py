import RPi.GPIO as GPIO
import time
import convert

INPUT_PIN = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(INPUT_PIN, GPIO.IN)

message = ""
wait = 0.1

#initialize input to zero. On program start, assume no voltage
bit = 0
receiving = False

def parseMessage(message):
    print("Raw Binary Data:")
    print(message)
    print("Converting.....")
    message = convert.parseSignal(message)
    print("Converted Message:")
    print(message)
    print("Saving to data.txt....")
    data = open('data.txt','w')
    data.write(message)
    data.close()
    print("All done!")

def onEdgeDetect(channel):
    if(GPIO.input(INPUT_PIN)):
        bit = 1
        return
    bit = 0

GPIO.add_event_detect(INPUT_PIN, GPIO.BOTH, callback=onEdgeDectect, bouncetime=100)

while(1):
    character = character + str(bit)
    if (len(character) == 8 ):
        print(character)
        if (convert.startT() == character and not recieving):
            recieving = True
	elif (convert.endT() == character and recieving):
	    message = message + character
	    parseMessage()
            recieving = False
            break
        elif(recieving):
	    message = message + character
	    character = ""
	time.sleep(waiti)

GPIO.cleanup()
