import time
import pycom as pyc #might not be correct import!

isRunning = True
isLightOn = False 
sendAsciiMode = False
ledColor = ""

while (isRunning):
    print('*** Main Menu ***')

    
    if(isLightOn == True):
        print("To change the color write the color value in HEX")

    print("To turn on light type 'on'")
    print("To turn off light type 'off'")

    userInput = input()
    if(userInput == "on"):
        pyc.rgbled('0xFFFFFF')
    if(userInput == 'off'):
        pyc.rgbled('0x000000')
    if(userInput == 'exit'):
        isRunning = False
    else:
        pyc.rgbled(ledColor)