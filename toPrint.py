#! /usr/bin/env python
#This is script is to manage the files being sent over to the printer

import shutil
import os
import time
import checkdir
import pickle

printButton=0 #will be changed to one when user clicks print button
with open('setup.inf') as n
	pickle.dump([DirLoc],n)
File=str(DirLoc+checkdir.Queue1)
printer=/path/to/printer
while 1=1:
	if printButton=1:
		while File!=str(DirLoc) #returns files to print:
			shutil.move(File, printer) #need to find out how printer processes files to send them over correctly
			os.remove(File)
		
	else:
		time.sleep(1) 

