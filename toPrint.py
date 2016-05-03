#! /usr/bin/env python
#This is script is to manage the files being sent over to the printer

import shutil
import os
import time
import checkdir

printButton=0 #will be changed to one when user clicks print button
File=File
directoryPath=/path/to/directory
printer=/path/to/printer
while 1=1:
	if printButton=1:
		checkdir...  #check staging directory for files
		while checkdir #retuturns files to print:
			shutil.move(directoryPath+File, printer) #need to find out how printer processes files to send them over correctly
			os.remove(directoryPath+File)
		
	else:
		time.sleep(1) #needs to be changed to trigger

