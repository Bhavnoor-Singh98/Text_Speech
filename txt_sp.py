from gtts import gTTS                 #Google Text-to-Speech  Library

import os

f=open("newfile.txt")                 #File where text is written
x=f.read()
lan="en"                              #You Can change your Language
                                      #storing Audio message
ad=gTTS(text=x,lang=lan,slow=False)   #Creating Audio file
ad.save("1.wav")  
os.system("1.wav")
