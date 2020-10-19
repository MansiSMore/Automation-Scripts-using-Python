#Assignment10_1.py

from sys import *
import os

def DirectoryFileSearch(pathname , extension):

	if(os.path.isabs(pathname) == False):				##Checking for absolute path
		pathname = os.path.abspath(pathname)

	chkdir = os.path.isdir(pathname)					##Checking for directory
	if chkdir == True :
		for foldername , subfolder , filename in os.walk(pathname):
			print("Files from folder : "+os.path.relpath(pathname))

			#for sub in subfolder:
				#print("You are inside "+sub+" folder : ")
			for fn in filename:
				if(fn.endswith(extension)):
					print(fn)

	else:
		print("Directory not found..!")



def main():
	if(len(argv) > 3 ):
		print("My_Error : Invalid no of Arguments...!")
		exit()

	if(len(argv) == 2):
		if(argv[1] == "-h" or argv[1] == "-H"):			##This option is for help.
			print("My_Help : This Scripts display files with the given extension.")
			exit()

		elif (argv[1] == "-u" or argv[1] == "-U"):		#This option is for demonstrating the syntax that user want to enter.
			print("My_Usage : Filename.py Directory_Name Specific_Extension")
			exit()

		else:
			print("My_Error : Wrong Arguments...!")
			exit()

	try:
		DirectoryFileSearch(argv[1],argv[2])

	except Exception as eobj:
		print(eobj)

if __name__ == "__main__":
	main()