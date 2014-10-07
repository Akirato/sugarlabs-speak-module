#! /usr/bin/python

import subprocess
import os
import sys
 
def say(words):
    tempfile = "temp.wav"
    devnull = open("/dev/null","w")
    subprocess.call(["pico2wave", "-w", tempfile, words],stderr=devnull)
    subprocess.call(["aplay", tempfile],stderr=devnull)
    os.remove(tempfile)

if len(sys.argv)<=1:
    say('Hello, you need put the sentence as an argument')
 
elif os.path.isfile(sys.argv[1]):
    fi=open(sys.argv[1],'r')  
    text=fi.read()
    say(text)

else:
    sentence=""
    for i in range(1,len(sys.argv)):
	sentence=sentence+sys.argv[i]
    say(sentence)



