# this code exists thanks to Texas-Mark on the official RPi forums, he shared the code the original iteration of this was (heavily) based on at https://www.raspberrypi.org/forums/viewtopic.php?t=176241

import RPi.GPIO as GPIO
import time
import os
import random


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 21 # GPIO pin 21
button = 18 # GPIO pin 18

GPIO.setup(led,GPIO.OUT) # sets up pin 21 to output
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP) #sets up pin 18 as a button

myCmd1 = 'omxplayer -o alsa lincoln.mp3'
myCmd2 = 'omxplayer -o alsa lincoln2.mp3'
myCmd3 = 'omxplayer -o alsa lincoln3.mp3'
myCmd4 = 'omxplayer -o alsa lincoln4.mp3'
myCmd5 = 'espeak "John Todd Stuart lent me books"'
myList = [myCmd1, myCmd2, myCmd3, myCmd4, myCmd5]
i_count = 0

GPIO.setup(pir_sensor, GPIO.IN, GPIO.PUD_DOWN)

current_state = 0
GPIO.setup(led,GPIO.OUT)

while True:
        input_state = GPIO.input(button) # primes the button!
        if input_state == False:
            i_count = i_count + 1
            GPIO.output(led,True) #Turn on LED
            os.system(random.choice(myList)) # play sound file
            GPIO.output(led,False) #turn off LED
            if i_count == 1:
                print("History Bot has been activated " + str(i_count) + " time!")
            else:
                print("History Bot has been activated " + str(i_count) + " times!")
            time.sleep(0.2)
