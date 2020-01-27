#This code was developed by Roby Mullins and Josh West for educational purposes.
#Much of our code is borrowed from other sources who attributed before the relevant code is used.

#This code runs the individual scripts simoultaneously for our Pliny. This code was inspired from the following links: 
#https://www.raspberrypi.org/forums/viewtopic.php?t=26777
#https://www.youtube.com/watch?v=c0HmVqsynrk

#! /bin/bash
python /home/pi/Desktop/VolcanoCode/VesuviusCode/VolcanoButton.py &
python /home/pi/Desktop/VolcanoCode/VesuviusCode/speechRecognition.py
