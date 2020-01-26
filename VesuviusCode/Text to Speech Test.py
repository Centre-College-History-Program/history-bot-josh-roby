import os
import time

message = "Hello Josh! How is your day today."

print('Festival Text to Speech')

os.system('echo "' + 'Festival Text to Speech demo' + '" | festival --tts')


time.sleep(1)


os.system('echo "' + message + '" | festival --tts')


time.sleep(1)






print('Espeak Text to Speech')


os.system('espeak -ven+f3 -k5 -s150 "' + 'Espeak Text to Speech demo' + '"')


time.sleep(1)


os.system('espeak -ven+f3 -k5 -s150 "' + message + '"')


time.sleep(1)






print('Pico Text to Speech')


os.system('pico2wave -w voice.wav "' + 'Pico Text to Speech demo' + '" && aplay voice.wav')


time.sleep(1)


os.system('pico2wave -w voice.wav "' + message + '" && aplay voice.wav')


time.sleep(1)
