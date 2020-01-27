#RGB LED Code

#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False) # Avoids warning channel is already in use

colors = [0x00BEFF, 0x00BEFF, 0x007DFF, 0x007DFF, 0x007DFF, 0x00C8FF, 0x00C8FF, 0x00FFFF, 0x00FFFF]
#        lightyellow           yellow     yellow    yellow    orange    orange     red      red        

#colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF, 0xFF6A00]
#            blue     pink     yellow     dark blue  green    red        blue
#, 0x22222B, 0x22222B  Dark Red
#0x00A6FF, 0x00A6FF, Dark Orange
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
        #print('inside while loop')
        for col in colors:

            #print('inside for loop')
            setColor(col)
            time.sleep(0.5)

except KeyboardInterrupt:
    p_R.stop()
    p_G.stop()
    p_B.stop()
    #p_O.stop()

    for i in pins:
        GPIO.output(pins[i], GPIO.HIGH) # Turn off all leds

    GPIO.cleanup()

