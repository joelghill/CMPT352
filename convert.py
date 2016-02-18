"""
Python script to convert to and from binary signals
"""

def stringToBinary(str):
    out = ''
    for letter in str:
        """
        print str(bin(ord(letter)))[2:]
        """
        out = out + charToBinary(letter)
    return out
        

def charToBinary(c):
    
    b = '{0:b}'.format(ord(c))
    if(len(b)<8):
        remaining = 8 - len(b)
        pre = ""
        for index in range(0,remaining):
            pre = pre + '0'
    return pre + b

def endT():
    return '00000' + '{0:b}'.format(4)


def binToChar(b):
    return chr(int(b,2))


def generateSignal(s):
    return '1' + stringToBinary(s) + endT()


def parseSignal(signal):
    count = 0
    temp = ''
    out = ''
    for b in signal:
        temp = temp + b
        if(len(temp) == 8):
            if(temp == endT()):
                return out
            else:
                out = out + binToChar(temp)
                temp=''
    return out
    

"""
t = stringToBinary("test")
print(t)
print('Length of binary string:  ' + str(len(t)))
print('EndT:  ' + endT())
signal = generateSignal('Another rather difficult string....')
print(signal)
print(parseSignal(signal[1:]))
"""
