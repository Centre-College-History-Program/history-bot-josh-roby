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
                wordList = text.lower().split() #makes a list of the words spoken
                #print("words: " + str(wordList)) #prints wordList, for sanity
                
                keys = ['birthday', 'born', 'death','die','died','kill','killed','nephew','younger','family', 'volcano','hi', 'hello','from','job','career','natural history',\
                        'natural','history','book','books','emperor','erupt','eruption','live','elder','who']
                answerDict = {"birthday": "My birthyear is 23 Ae D", "born": "I was born in 23 Ae D", "death": "I met my death August 24, 79 Ae D",
                              "die": "I died on August 24, 79 Ae D from asphyxiatiion due to volcanic ash from the eruption of Mount Vesuvius", "died": "I died on August 24, 79 Ae D",
                              "kill": "I was killed by the ash from the eruption of Mount Vesuvius on August 24, 79 Ae D",
                              "killed": "I was killed by the ash from the eruption of Mount Vesuvius on August 24, 79 Ae D",
                              "nephew": "My nephew was Pliny the younger. He helped preserve my legacy by writing about me. I helped raised him. He was not as ambitious as me as he only became a lawyer, but he was a good kid.",
                              "younger": "Pliny the younger was my nephew. I helped raise him and in return he preserved my legacy by writing about me. He was not as ambitious as me as he only became a lawyer, but he was a good kid.",
                              "family": "My sister and her son, Pliny the younger, were very important to me. Pliny the younger preserved my legacy by writing about me.",
                              "volcano": "Mount Vesuvius was the volcano that erupted and destroyed Pompeii.",
                              "hi": "Hi, my name is Pliny the Elder.",
                              "hello": "Hello, my name is Pliny the Elder.",
                              "from": "I'm from northern Italy, near Gaul. I was stationed in Naples when the eruption occured.",
                              "job": "I served in the equestrian branch of the Roman legion. I also served as a governor of Roman provinces accross the empire. In my free time I wrote over 100 books, including Natural History.",
                              "career": "I served in the equestrian branch of the Roman legion. I also served as a governor of Roman provinces accross the empire. In my free time I wrote over 100 books, including Natural History.",
                              "natural": "Natural History is my only surviving volume of books in which I cover various topics such as: geology, geography, ethnography, astronomy, botany, zoology, and more.", "history": "Some say that my role in history was essential to Europe's immersion from the dark ages. But there are many who don't know me at all. I think this should change, don't you?",
                              "book": "Natural History is my only surviving volume of books in which I cover various topics such as: geology, geography, ethnography, astronomy, botany, zoology, and more.",
                              "books": "Natural History is my only surviving volume of books in which I cover various topics such as: geology, geography, ethnography, astronomy, botany, zoology, and more.",
                              "emperor": "I lived during the time of Emporer Nero, an idiotic and violent emporer that did not support the quest for information.",
                              "erupt": "Vesuvius is an active volcano and is projected to erupt again within the next two to three decades.",
                              "eruption": "The vesuvius eruption destroyed many cities with Herculenaeum and Pompeii being the two best preserved and was more powerful than two of your atomic bombs.",
                              "live": "Rome is a glorius, strict empire that provides security for its citizens against the harsh unforgiving world.",
                              "elder": "I served for most of my adult life in the equestrian branch of the Roman military working my way up the meritocracy from humble beginnings to officer status and eventually to a procurratorship, a governorship, of several different Roman provinces in Spain, Africa, the Middle East, and Italy. I used my position to pursue my love of education and information to amass a great wealth of knowledge and write over 100 books."

                }
                hitcount = 0
                for word in wordList:#goes through spoken words
                    #print("word in text")
#                     for key in keys:#goes trhough the lsit of keys
#                         print("key in keys")
                    if word in keys:#check if the word is a key
                        #print("word in keys")
                        hitcount+=1 #increase the hit count for this word
                        print("Pliny's answer: " + answerDict.get(word)) #prints Pliny's answer to the question
                        os.system('espeak -ven+f3 -k5 -s150 "' + answerDict.get(word) + '"') #speaks Pliny's answer
                    elif word == "vesuvius":
                        print("rumble rumble")
                        os.system('omxplayer -o alsa /home/pi/Desktop/VolcanoCode/VesuviusCode/Vesuvius.mp3')
                        
                #print('hitcount: ', hitcount)
            except Exception as e:
                print("I'm sorry I didn't understand you. Please come closer.")
                print(e)
    #print("I'm free of that WHILE")
    
            
