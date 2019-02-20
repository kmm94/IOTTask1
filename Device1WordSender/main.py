import time
import pycom as pyc #might not be correct import!
import binascii

#This used to send ascii carraktor to an ambient ligte sensor 

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def LightOnOneSec():
    pyc.rgbled('0xFFFFFF')
    time.sleep(1)

def LightOffOneSec():
    pyc.rgbled('0x000000')
    time.sleep(1)

def InitiateConnection():
    pyc.rgbled('0xFFFFFF')
    time.sleep(5)

def SignalEndText():
    pyc.rgbled('0x000000')
    time.sleep(8)


isRunning = True
ledColor = ""

while (isRunning):
    print('*** Main Menu ***')
    print("Type the text that you want to send: ")
    print("Type 'Exit' to EndProgram")
    text = input()
    if(text == 'Exit'):
        break
    bitString = text_to_bits(text)
    InitiateConnection()
    for bit in bitString:
        if(bit == "0"):
            LightOffOneSec()
        elif bit == "1":
            LightOnOneSec()
    SignalEndText()


