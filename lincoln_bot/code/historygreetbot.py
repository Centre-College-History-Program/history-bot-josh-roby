# this code exists thanks to Texas-Mark on the official RPi forums, he shared the code this is (heavily) based on at https://www.raspberrypi.org/forums/viewtopic.php?t=176241

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pir_sensor = 4 #GPIO pin 4
led = 21 #GPIO pin 21
myCmd = 'omxplayer -o alsa lincoln.mp3'

GPIO.setup(pir_sensor, GPIO.IN, GPIO.PUD_DOWN)

current_state = 0
GPIO.setup(led,GPIO.OUT)

while True:
    try:
        time.sleep(0.1)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
          print("Lincoln Bot Activated") # motion detected
          os.system(myCmd) # plays the mp3
          GPIO.output(led,True) #Turn on LED
          time.sleep(2) # leave LED on for 2 seconds
          GPIO.output(led,False) #turn off LED
          time.sleep(4) # wait 4 seconds for PIR to reset. 
    except KeyboardInterrupt:
        GPIO.cleanup()
        
