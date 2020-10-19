#Text to Speech API from Google

import gtts
import urllib.request

def Connection_Established():
	try:
		urllib.request.urlopen("https://www.google.com/",timeout = 5)
		#print(url)
		#If we connect with specified url,then return True otherwise throw Exception.
		return True
	except Exception as eobj:
		raise eobj


try:
	#print(34)
	connect = Connection_Established()
	
	#print(12)
	#Languages from GTTS
	languages = gtts.lang.tts_langs()
	#print(languages)

	#for key,value in languages.items():
	#print(key+" : "+value)

	print("Enter text : ")
	str = "Welcome Back Mansi"
	
	print("Opening mansi.mp3......")	
	tobj = gtts.gTTS(str, lang='en')
	tobj.save('Mansi.mp3')
 
	#This statement is for automatically opening file
	import os
	os.system("Mansi.mp3")

except Exception as eobj:
	print("Connection Error...!",eobj)