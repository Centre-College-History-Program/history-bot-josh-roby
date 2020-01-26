#This script is for speech recognition on the Raspberry Pi 3B+
import speech_recognition as sr
import os
import time

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
            print("Talk Pliny to me. I'm listening . . .")#prompts user to speak
            audio = r.listen(source)#audio from mic that user speaks
            
            try:
                print("I'm thinking . . .")
                text = r.recognize_google(audio)
                print("You said: " + text) #prints what the person said
                wordList = text.split() #makes a list of the words spoken
                print("words: " + str(wordList)) #prints wordList, for sanity
                
                keys = ['birthday', 'born', 'death','die','died','kill','killed','nephew','younger','family', 'volcano','hi', 'hello']
                answerDict = {"birthday": "My birthyear is 23 Ae D", "born": "I was born on 23 Ae D", "death": "I met my death August 24, 79 Ae D",
                              "die": "I died on August 24, 79 Ae D", "died": "I died on August 24, 79 Ae D",
                              "kill": "I was killed by the ash from the eruption of Mount Vesuvius on August 24, 79 Ae D",
                              "killed": "I was killed by the ash from the eruption of Mount Vesuvius on August 24, 79 Ae D",
                              "nephew": "My nephew was Pliny the younger. He helped preserve my legacy by writing about me. I helped raised him. He was not as ambitious as me as he only became a lawyer, but he was a good kid.",
                              "younger": "Pliny the younger was my nephew. I helped raise him and in return he preserved my legacy by writing about me. He was not as ambitious as me as he only became a lawyer, but he was a good kid.",
                              "family": "My sister and her son, Pliny the younger, were very important to me. Pliny the younger preserved my legacy by writing about me.",
                              "volcano": "Mount Vesuvius was the volcano that erupted and destroyed Pompeii.",
                              "hi": "Hi, my name is Pliny the Elder.",
                              "hello": "Hello, my name is Pliny the Elder."}
                hitcount = 0
                for word in wordList:#goes through spoken words
                    print("word in text")
#                     for key in keys:#goes trhough the lsit of keys
#                         print("key in keys")
                    if word in keys:#check if the word is a key
                        print("word in keys")
                        hitcount+=1 #increase the hit count for this word
                        print("Pliny's answer: " + answerDict.get(word)) #prints Pliny's answer to the question
                        os.system('espeak -ven+f3 -k5 -s150 "' + answerDict.get(word) + '"') #speaks Pliny's answer
                    elif word == "Vesuvius":
                        print("rumble rumble")
                        os.system('omxplayer -o alsa /home/pi/Desktop/VolcanoCode/VesuviusCode/Vesuvius.mp3')
                        
                #print('hitcount: ', hitcount)
            except:
                print("I'm sorry I didn't understand you. Please come closer.")
    #print("I'm free of that WHILE")
    
            
