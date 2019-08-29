# example taken from https://maker.pro/raspberry-pi/tutorial/how-to-interface-a-pir-motion-sensor-with-raspberry-pi-gpio
# this just gets an LED to blink, as title implies

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)     #Define pin 3 as an output pin

while True:
GPIO.output(3,1)   #Outputs digital HIGH signal (5V) on pin 3
time.sleep(1)      #Time delay of 1 second

GPIO.output(3,0)   #Outputs digital LOW signal (0V) on pin 3
time.sleep(1)      #Time delay of 1 second
