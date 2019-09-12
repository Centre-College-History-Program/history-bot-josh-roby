# John Harney, Centre College, 09.10.19

# this code exists thanks to Texas-Mark on the official RPi forums, 
# he shared the code the original (PIR sensor) iteration of this was based on at 
# https://www.raspberrypi.org/forums/viewtopic.php?t=176241

# button code version relied heavily on Soren at 
# https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/

import RPi.GPIO as GPIO
import time
import os
import random

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # use gpio numbering

led = 21 # GPIO pin 21
myCmd1 = 'omxplayer -o alsa kennedy1.mp3' # These examples are from the "Kennedy bot"
myCmd2 = 'omxplayer -o alsa kennedy2.mp3' # Change 
myCmd3 = 'omxplayer -o alsa kennedy3.mp3' # as
myCmd4 = 'omxplayer -o alsa kennedy4.mp3' # needed
myList = [myCmd1, myCmd2, myCmd3, myCmd4] 

# set pin 20 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) 


current_state = 0
GPIO.setup(led,GPIO.OUT)

while True:
    try:
        time.sleep(0.1)
        if GPIO.input(20) == GPIO.HIGH:
          GPIO.output(led,True) #Turn on LED
          os.system(random.choice(myList)) # plays one of the mp3 files
          GPIO.output(led,False) #turn off LED
    except KeyboardInterrupt:
        GPIO.cleanup()
