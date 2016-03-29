import RPi.GPIO as GPIO
import time
import convert

INPUT_PIN = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(INPUT_PIN, GPIO.IN)

message = ""
wait = 0.01
character = [0,0,0,0,0,0,0,0]
count = 0

#initialize input to zero. On program start, assume no voltage
bit = 0
recieving = False

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

def arrayToString(array):
    return ''.join(str(x) for x in array)

def onEdgeDetect(channel):
    global bit
    if(bit == 0):
        bit = 1
        return
    bit = 0

GPIO.add_event_detect(INPUT_PIN, GPIO.BOTH, callback=onEdgeDetect)

while(1):
    character.pop(0)
    character.append(bit)
    if(convert.startT() == arrayToString(character) and not recieving):
        recieving = True
        print("RECIEVED START CHARACTER")
        count = 0
        recieving = True
    elif (convert.endT() == arrayToString(character) and recieving and count == 7):
	message = message + arrayToString(character)
	parseMessage(message)
        recieving = False
        break
    elif(recieving and count == 7):
        print(arrayToString(character))
	message = message + arrayToString(character)
        count = 0
    elif(recieving):
        count = count + 1
    time.sleep(wait)

GPIO.cleanup()
