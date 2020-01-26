import RPi.GPIO as GPIO
import time
import os
import random
import subprocess
import rgbledtest as ledCode
import VolcanoButton as buttonCode
import speechRecognition as speechRecognitionCode

def main():
    #CODE GOES HERE
    while True:
        subprocess.Popen(["python",'ledCode'])
        time.sleep(0.1)
        subprocess.Popen(["python",'buttonCode'])
        #ledCode.main() #do whatever is in rgbledtest.py
        #buttonCode.main() #do whatever is in Volcano Button
        #speechRecognitionCode.main() #do whatever is in speech test.py
main()
