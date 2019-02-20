import time


# This is used to recive words from Device 1
# protocol is: 
# First the sender device led will be off
# to notify this unit to be ready to recive the sender device will turn on LED for 5 sec Followed by the message.
# The message will be send one bit at a time were 
# no ligth for one sec means 0 
# light for one sec means 1
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
ligthThreshold = 1000

while isRunning:
    print('Device is ready to recive')
    while(isReciving == False):
        lightTuple = lightsensor.light()
        lightIntensity = lightTuple[0]+lightTuple[1]
        if(lightIntensity > ligthThreshold):
            break
    print('reciving')
    timer = time.time
    while timer <= 5:
        timer = time.time
    
        
    



