import os
import time

message = "Pliny the Elder for United States President in the year of our lord 2020"

os.system('espeak -ven+f3 -k5 -s150 "' + message + '"')


time.sleep(1)
