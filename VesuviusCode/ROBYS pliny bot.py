#This code was developed by Roby Mullins and Josh West for educational purposes.
#Much of our code is borrowed from other sources who attributed before the relevant code is used.

#RGB LED Code; Code from INSERT WEBSITE HERE

#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import os
import random



#Button & Quotes Code
# John Harney, Centre College, updated 10.21.19

# this code exists thanks to Texas-Mark on the official RPi forums,
# he shared the code the original (PIR sensor) iteration of this was based on at
# https://www.raspberrypi.org/forums/viewtopic.php?t=176241

# button code version relied heavily on Soren at
# https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/

# this is the base code for all history bots as of 10.21.19


GPIO.setmode(GPIO.BOARD) #use the GPIO numbering
GPIO.setwarnings(False) # Avoids warning channel is already in use

led = 26 # GPIO pin 21
button = 18 # GPIO pin 18
button_led = 7 # GPIO pin 26
# positive of button_led = GPIO pin 1

GPIO.setup(led,GPIO.OUT) # sets up pin 21 to output
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP) #sets up pin 18 as a button
GPIO.setup(button_led,GPIO.OUT) #sets up pin 26 to output



myCmd1 = 'omxplayer -o alsa NoBook.mp3' # this clip was too low, changed volume
myCmd2 = 'omxplayer -o alsa Uncertain.mp3' # These examples are from the "Ali bot"
myCmd3 = 'omxplayer -o alsa HomeHeart.mp3' # change
myCmd4 = 'omxplayer -o alsa FortuneFavors.mp3' # as

myList = [myCmd1, myCmd2, myCmd3, myCmd4]
# GPIO.output(button_led, True) #turn on button LED

def LEDSCRIPT():
    colors = [0x007DFF, 0x007DFF, 0x007DFF, 0x00C8FF, 0x00C8FF,0x00FFFF, 0x00FFFF, 0x00FFFF]
    #         yellow     yellow    yellow    orange     orange   red      red        red
    
    #colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF, 0xFF6A00]
    #            blue     pink     yellow     dark blue  green    red        blue
    #0x000000 white
    #0xFF0000 cyan-ish

    pins = {'pin_R':11, 'pin_G':13, 'pin_B':15} # pins is a dict

    GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by BOARD

    for i in pins:
        GPIO.setup(pins[i], GPIO.OUT) # Set pins' mode is output
        GPIO.output(pins[i], GPIO.HIGH) # Set pins to high(+3.3V) to off led

    p_R = GPIO.PWM(pins['pin_R'], 2000) # set Frequece to 2KHz
    p_G = GPIO.PWM(pins['pin_G'], 2000)
    p_B = GPIO.PWM(pins['pin_B'], 2000)

#p_O = GPIO.PWM(pins['pin_R'+'pin_G'], 2000)

    p_R.start(0) # Initial duty Cycle = 0(leds off)
    p_G.start(0)
    p_B.start(0)
#p_O.start(0)


    def map(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def setColor(col): # For example : col = 0x112233
        R_val = (col & 0xFF0000) >> 16
        G_val = (col & 0x00FF00) >> 8
        B_val = (col & 0x0000FF) >> 0
    #O_val = (col & 0xFF4500) >> 0

        R_val = map(R_val, 0, 255, 0, 100)
        G_val = map(G_val, 0, 255, 0, 100)
        B_val = map(B_val, 0, 255, 0, 100)
    
    #O_val = map(O_val, 0,255, 69, 100)

        p_R.ChangeDutyCycle(R_val) # Change duty cycle
        p_G.ChangeDutyCycle(G_val)
        p_B.ChangeDutyCycle(B_val)


    try:

        while True:
            print('inside while loop')
            for col in colors:

                print('inside for loop')
                setColor(col)
                time.sleep(0.5)

    except KeyboardInterrupt:
        p_R.stop()
        p_G.stop()
        p_B.stop()
    #p_O.stop()

        for i in pins:
            GPIO.output(pins[i], GPIO.HIGH) # Turn off all leds

        #GPIO.cleanup()

while True:
    print ("Made it to the promised land")
    #LEDSCRIPT()
    GPIO.output(button_led, False) #turn on button LED
    input_state = GPIO.input(button)
    if input_state == False: #GPIO.event_detected(18):
        GPIO.output(button_led, True) # turns off button led
        print ("I could use a pint of guiness")
        os.system(random.choice(myList))
        time.sleep(.2)
    else: 
        print ("JK I love humans... for dinner")
        GPIO.output(button_led, False) # turn on button led
        time.sleep (.2)
    if True:
        LEDSCRIPT()
        
