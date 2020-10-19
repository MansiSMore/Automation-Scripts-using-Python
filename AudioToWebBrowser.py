
from sys import *
import webbrowser
import re
import urllib.request 
import speech_recognition as sr
from gtts import gTTS
                                                               
import urllib3
import os 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from pygame import mixer

def audioStart():
	
	mixer.init()
	#while (True):                                  #quiet the endless 'insecurerequest' warning
	r = sr.Recognizer()                                                     # obtain audio from the microphone
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source, duration=1)
		print("Enter your name:")
		x=input()
		print("Say something!")
		audio = r.listen(source,phrase_time_limit=10)
	
	try:
		response = r.recognize_google(audio)
		print("I think {} you said '".format(x) + response + "'")
		tts = gTTS(text="I think {} you said ".format(x)+str(response), lang='en')
		tts.save("response.mp3")
		file = "response.mp3" 
		mixer.music.load('response.mp3')
		os.system(file)#mixer.music.play()
		if str is bytes:
			result = u"{}".format(response).encode("utf-8")
		else:
			result = "{}".format(response)

		fname="outputs.txt"
		fp=open(fname,"w")#with open("outputs.txt","w") as f:
		fp.write(result)
		print(result)
	except sr.UnknownValueError:
		print("Sphinx could not understand audio")
	except sr.RequestError as e:
		print("Sphinx error; {0}".format(e))

def is_connected():
	print("Mumbai..!")
	try:
		urllib.request.urlopen('http://216.58.192.142',timeout=5)
		return True
	except urllib.request.URLError as err:
		return False

def Find(string):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',string)
    #print(url)
    return url

def WebLauncher(path):
    with open(path) as fp:
    	for line in fp:
        	line = line.replace(" ","")
        	#print(line)
        	url = Find(line)
        	#print(url)
        	for str in url:
        		webbrowser.open(str, new=2)

def main():

    print("Code is for audio to URL :::::::::")
    audioStart()
    try:
    	connected=is_connected()
    	if connected:
    		print("connection is done")
    		WebLauncher("outputs.txt")
    	else:
    		print("Unable to connect to Internet....!")

    except Exception as E:
    	print("Error:Invalid input...!",E)

if __name__=="__main__":
    main()
