# John Harney, Centre College, updated 10.21.19

# this code exists thanks to Texas-Mark on the official RPi forums,
# he shared the code the original (PIR sensor) iteration of this was based on at
# https://www.raspberrypi.org/forums/viewtopic.php?t=176241

# button code version relied heavily on Soren at
# https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/

# this is the base code for all history bots as of 10.21.19

import RPi.GPIO as GPIO
import time
import os
import random
import subprocess

GPIO.setmode(GPIO.BOARD) #use the GPIO numbering
GPIO.setwarnings(False) # Avoids warning channel is already in use

#led = 26 # GPIO pin 21
button = 18 # GPIO pin 18
button_led = 7 # GPIO pin 26
# positive of button_led = GPIO pin 1

#GPIO.setup(led,GPIO.OUT) # sets up pin 21 to output
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP) #sets up pin 20 as a button
GPIO.setup(button_led,GPIO.OUT) #sets up pin 26 to output

#myCmd0 = 'omxplayer -o alsa bell_test.mp3'
myCmd1 = 'omxplayer -o alsa /home/pi/Desktop/VolcanoCode/VesuviusCode/NoBook.mp3' # test clip
myCmd2 = 'omxplayer -o alsa /home/pi/Desktop/VolcanoCode/VesuviusCode/Uncertain.mp3' #pliny quotes
myCmd3 = 'omxplayer -o alsa /home/pi/Desktop/VolcanoCode/VesuviusCode/HomeHeart.mp3' 
myCmd4 = 'omxplayer -o alsa /home/pi/Desktop/VolcanoCode/VesuviusCode/FortuneFavors.mp3' 

myList = [myCmd1, myCmd2, myCmd3, myCmd4]
# GPIO.output(button_led, True) #turn on button LED
subprocess.Popen(["python",'/home/pi/Desktop/VolcanoCode/VesuviusCode/rgbledtest.py']) #runs the code for the rgb LED as a subprocess
print("button working")
while True:
    GPIO.output(button_led, False) #turn on button LED
    input_state = GPIO.input(button)
    if input_state == False: #GPIO.event_detected(18):
        GPIO.output(button_led, True) # turns off button led
        #print ("I could use a pint of guiness")
        os.system(random.choice(myList))
        time.sleep(.2)
    else: 
        #print ("JK I love humans... for dinner")
        GPIO.output(button_led, False) # turn on button led
        time.sleep (.2)
        