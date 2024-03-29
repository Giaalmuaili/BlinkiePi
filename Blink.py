#import Pi GPIO and time modules
import RPi.GPIO as GPIO
import time
 
#set up GPIO numbering and turn off warnings (don't worry if you don't understand this right now)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
#set up which pin to control the LED from and set it to output
ledPin = 12
GPIO.setup(ledPin, GPIO.OUT)
 
"""
This for loop runs the code inside it 5 times, change the number in the range() brackets to alter how many times it runs.
The LED turns on for half a second, then turns off again.
Make sure you indent the code inside the for loop correctly!
"""
 
for i in range(5):
    print("LED turning on")
    GPIO.output(ledPin,GPIO.HIGH)
    time.sleep(0.5)
    print("LED turning off")
    GPIO.output(ledPin,GPIO.LOW)
    time.sleep(0.5)