import time
import pycom as pyc #might not be correct import!
import binascii
import EncoderDecoder

#This used to send ascii carraktor to an ambient ligte sensor 

# Method to encode the text to binary
def getBitValue(letter):
    bitvalue = ""
    bitvalue = EncoderDecoder.dataEncoding[letter]
    return bitvalue

def textToBits(text):
    BitString = "" 
    for letter in text:
        BitString += getBitValue(letter)
    return BitString

#turns light on for one sec
def LightOn():
    pyc.rgbled(0xFFFFFF)
#turns light off for one sec
def LightOff():
    pyc.rgbled(0x000000)

#Sends the startConnection pattern
def InitiateConnection():
    pyc.rgbled(0xFFFFFF)
    time.sleep(5)

#Send end of transsmission signal
def SignalEndText():
    pyc.rgbled(0x000000)
    time.sleep(8)

def Wait():
    time.sleep(1)

pyc.heartbeat(False)
isRunning = True
ledColor = ""

while (isRunning):
    print('*** Main Menu ***')
    print("Type the text that you want to send: ")
    print("Type 'Exit' to EndProgram")
    text = input()
    if(text == 'Exit'):
        break
    if(text != ""):
        bitString = textToBits(text)
        print(bitString)
        InitiateConnection()
        for bit in str(bitString):
            print("sending: " + bit)
            if(bit == "0"):
                LightOff()
                Wait()
            elif bit == "1":
                LightOn()
                Wait()
        SignalEndText()


