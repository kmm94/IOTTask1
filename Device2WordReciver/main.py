import time
import pycom

# This is used to recive words from Device 1
# protocol is: 
# First the sender device led will be off
# to notify this unit to be ready to recive the sender device will turn on LED for 5 sec Followed by the message.
# The message will be send one bit at a time were 
# no ligth for one sec means 0 
# light for one sec means 1
# Each letter is 8 bits!
# the message will end with the LED being turn off for 8 sec


# From:https://github.com/pycom/pycom-libraries
from LTR329ALS01 import LTR329ALS01
from SI7006A20 import SI7006A20
from pytrack import Pytrack

py = Pytrack()
lightsensor = LTR329ALS01()
humiAndTempSensor = SI7006A20()
isRunning = True
isReciving = False
ligthThreshold = 200

def bitLen(int_type):
    length = 0
    while (int_type):
        int_type >>= 1
        length += 1
    return(length)

#Metode to decode a lettere from a byte
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((bitLen(n) + 7) // 8, 'big').decode(encoding, errors) or '\0'

#Method to recive the ligth intensity, the board have 2 sensor which is add and then returned
def getLightIntensity():
    lightTuple = lightsensor.light()
    lightIntensity = lightTuple[0]+lightTuple[1]
    return lightIntensity

# Method reads the light intensity and waites one second before returning the bit
# if the lightintensity is above the ligthTreshold the methode returns 1
# if the lightintensity is below the ligthTreshold the methode returns 0
def sampleOneSecond():
    if(getLightIntensity() > ligthThreshold):
        time.sleep(1)
        return "1"
    else:
        time.sleep(1)
        return "0"


pycom.heartbeat(False)
recivedText = ""

while isRunning:
    print('Device is ready to recive')
    print("waiting for signal...")
    while(isReciving == False): # Sampling the lightIntensity, waiting for the start signal which is ligth on for 5 sec
        if(getLightIntensity() > ligthThreshold):
            recivedText = ""
            isReciving = True
            break
    print('reciving')
    startTime = time.time()
    timer = 0

    while timer < 6: # Waiting 5 sec for the start signal to end
        timer = time.time() - startTime
        # Alternertive the start signal could be changed to 5 sec on follow by off 1 sec then the device could sync the moment the ligth turns off 
    
    counter = 0 #counting bits recived
    byte = ""
    while isReciving: 
        counter +=1
        bit = sampleOneSecond() 
        byte += bit
        print("Recived: " + bit + " Collecting Byte: " +byte)
        if(byte == "00000000"): #End Pattern
            isReciving = False
            print("An 'End of transsmission' was recived connection terminated")
            print("Text Recived:")
            print(recivedText)
            break

        if(counter >= 8): #Putting 8 bits together to form one byte
            recivedText += text_from_bits(byte)
            print("Text recived so far:")
            print(recivedText)
            counter = 0
            byte = ""



    





