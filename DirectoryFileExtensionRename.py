#Assignment10_2.py

from sys import *
import os

def ExtensionRename(pathname,ext1,ext2):
	
	if(os.path.isabs(pathname) == False):				
		pathname = os.path.abspath(pathname)

	chkdir = os.path.isdir(pathname)

	dirarr = os.listdir(pathname)

	print("Names before changes : ",dirarr)
	if(chkdir):
		for fname in dirarr:
			if(fname.endswith(ext1)):
				name , ext = os.path.splitext(fname)
				os.rename(os.path.join(pathname,fname),os.path.join(pathname,name+ext2))

	else:
		print("Directory not found..!")

	print("Changes updated...!")
def main():
	if(len(argv) > 4):
		print("My_Error : Invalid no of Arguments...!")
		exit()

	if(len(argv) == 3):
		print("My_Error : Required one more argument...!")
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
		ExtensionRename(argv[1],argv[2],argv[3])

	except Exception as eobj:
		print(eobj)


if __name__ == "__main__":
	main()
