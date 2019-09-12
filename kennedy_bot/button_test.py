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

GPIO.setmode(GPIO.BCM) #use the GPIO numbering
GPIO.setwarnings(False) # Avoids warning channel is already in use

led = 21 # GPIO pin 21
button = 18 # GPIO pin 18

GPIO.setup(led,GPIO.OUT) # sets up pin 21 to output
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP) #sets up pin 18 as a button

myCmd1 = 'omxplayer -o alsa /home/pi/kennedy_bot/kennedy1.mp3' # These examples are from the "Kennedy bot"
myCmd2 = 'omxplayer -o alsa /home/pi/historybots/kennedy_bot/kennedy2.mp3' # Change 
myCmd3 = 'omxplayer -o alsa /home/pi/historybots/kennedy_bot/kennedy3.mp3' # as
myCmd4 = 'omxplayer -o alsa /home/pi/historybots/kennedy_bot/kennedy4.mp3' # needed
myList = [myCmd1, myCmd2, myCmd3, myCmd4] 

while True:
        input_state = GPIO.input(button) # primes the button!
        if input_state == False:
            print("History Bot Activated!")
            GPIO.output(led,True) #Turn on LED
            os.system(random.choice(myList)) # play sound file
            GPIO.output(led,False) #turn off LED
            time.sleep(0.2)

