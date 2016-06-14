#! /usr/bin/env python3
#This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, #You can obtain one at https://mozilla.org/MPL/2.0/

'''
checkdir_v2_p3.py uses Python3, its just an update from the 
previous printer queue from list version, and also contains 
the Name/ID of the printers.
'''


####### IMPORTS #######

import os
import pickle
from tkinter import *
from tkinter import filedialog
import re
import subprocess
import sys
import importlib




#######VARIABLES########

#Add on to the devices by adding to the list in the categories. make sure the element index is the same
Printers = {
        'DeviceName':["Ultimaker2","Bukito","Red Wheel Mouse"],
        'ID': ["2341:0042","16c0:0483","04b3:310b"]
        }



####### FUNCTIONS #######	

#What is this function for? Meta-programming? No need for it I think
'''
def WriteToQueue():
	importlib.reload(PrinterQueue)
	
	filePath = filedialog.askopenfilename()
	currentFilePath=PrinterQueue.CurrentFilePath()
	currentFilePath.append(filePath)
	n=int(0)
	revfilepath=filePath[::-1]
	while n<int(len(filePath)):
		if str(revfilepath[n])=="/":
			n=int(len(filePath)-n)
			break
		else:
			n+=1
	fileName=filePath[n:len(filePath)]
	currentFileName=PrinterQueue.CurrentFileName()
	currentFileName.append(fileName)
	with open("PrinterQueue.py", "w") as f: 
		f.write("""#! /usr/bin/env python3
#This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, #You can obtain one at https://mozilla.org/MPL/2.0/

def CurrentFileName():
	currentFileName=""")
		f.write(str(currentFileName))
		f.write("""
	return currentFileName
def CurrentFilePath():
	currentFilePath=""")
		f.write(str(currentFilePath))
		f.write("""
	return currentFilePath
def CurrentPrintNumber():
	currentPrintNumber=""")
		f.write(str(currentPrintNumber))
		f.write("""
	return currentPrintNumber
def CurrentPrintType():
	currentPrintType=""")
		f.write(str(currentPrintType))
		f.write("""
	return currentPrintType
CurrentFileName()
CurrentFilePath()
CurrentPrintNumber()
CurrentPrintType()""")
	importlib.reload(PrinterQueue)
def DeleteFromQueue(index):
	with open("PrinterQueue.py", "w") as f: 
		f.write("""#! /usr/bin/env python3
#This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, #You can obtain one at https://mozilla.org/MPL/2.0/

def CurrentFileName():
	currentFileName=""")
		f.write(str(currentFileName))
		f.write("""
	return currentFileName
def CurrentFilePath():
	currentFilePath=""")
		f.write(str(currentFilePath))
		f.write("""
	return currentFilePath
def CurrentPrintNumber():
	currentPrintNumber=""")
		f.write(str(currentPrintNumber))
		f.write("""
	return currentPrintNumber
def CurrentPrintType():
	currentPrintType=""")
		f.write(str(currentPrintType))
		f.write("""
	return currentPrintType
CurrentFileName()
CurrentFilePath()
CurrentPrintNumber()
CurrentPrintType()""")
	importlib.reload(PrinterQueue)

'''
	
def GetUSB():  #we have to find a replacement for this, unfortunately I can't access Windows' commands
	device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
	if os.name == 'nt':
		#df = subprocess.check_output("lsusb", shell=True) windows equivelent
		pass
	else:
		df = subprocess.check_output("lsusb", shell=True)
	devices = []
	for i in df.split():
		if i:
			info = device_re.match(i)
			if info:
				dinfo = info.groupdict()
				dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
				devices.append(dinfo) 
	#ID=PrinterRainbowTable.Device()
	#DeviceName=PrinterRainbowTable.DeviceName()
	n=int(0)
	while int(len(devices)-1)>=n:
		dID=devices[n]
		m=int(0)
		while int(len(ID)-1)>=m:
			if dID['id']==ID[m]:
				Printer=DeviceName[m]
				Printer.append(dID['device'])
			if int(len(devices)-1)==n and int(len(devices)-1)==m :
				Printer="null"
			m+=1
		n+=1
	return Printer #this is the path to the printer

####### MAIN SCRIPT #######


class Application(Frame):
	def ConnectToPrinter(self):
		port=GetUSB()
		found=port[0]
		print (port)
		if port==str("null"): #Weather the printer is connected or not needs to be displayed in the GUI
			print ("No printer was found.")
		else:
			n=int(1)
			while n<found:
				print (port[n],"Printer found.")
				n+=2
		#with open(port,"rb") as f:
			#	data=f.read()
			#	printerbinary=data.encode('ascii')
			#print printerbinary  #CDH How do you work with pure binary data in pyhton?

	def AddToQueue(self):	
		#WriteToQueue()
		fileName=PrinterQueue.CurrentFileName()
		fileName=fileName[int(len(fileName)-1)]
		self.QueueList.insert(END,fileName)
		

	def RemoveFromQueue(self):
		index = self.QueueList.index(ACTIVE)
		print(self.QueueList)
		#DeleteFromQueue(index)
		self.QueueList.delete(index)

	def MakeNormal(self):
		root.wm_state('normal')

	def SendToPrinter(self):
		print ("functionality")

	def MoveUp(self):
		l = self.QueueList
		try:
			pos = list(l.curselection())[0]
		except:
			return
		if pos == 0:
			print ("is zero")
			return
		text = l.get(pos)
		l.delete(pos)
		l.insert(pos-1, text)
		l.selection_set(pos-1)

	def MoveDown(self):
		l = self.QueueList
		try:
			pos = list(l.curselection())[0]
		except:
			return
		if pos == len(l.get(0, END))-1:
			print ("is end")
			return
		text = l.get(pos)
		l.delete(pos)
		l.insert(pos+1, text)
		l.selection_set(pos+1)

	def LoopDir(self):
		PrintList =PrinterQueue.CurrentFileName()
		if PrintList != self.CompareList:
			try:
				if len(PrintList) > len(self.CompareList):  ##something needs to be added
					temp = list(set(PrintList) - set(self.CompareList))
					for i in temp:
						self.QueueList.insert(END,i)

				elif len(PrintList) < len(self.CompareList):   ##something needs to be removed
					temp = list(set(self.CompareList) - set(PrintList))
					for i in temp:
						gone = self.CompareList.index(i)
						self.QueueList.delete(gone)
				elif set(PrintList) == set(self.CompareList):
					pass
				else:   ##Something bad happened, reset list
					self.QueueList.delete(0, END)
					for i in PrintList:
						self.QueueList.insert(END,i)
			except:
				print ("something wrong")

		currentQueue = list(self.QueueList.get(0,END))

		self.CompareList = self.QueueList.get(0,END)
		self.after(1000, self.LoopDir)

	def createWidgets(self):

		self.printqueue = Button(self)
		self.printqueue["text"] = "Print Queue",
		self.printqueue["command"] = self.SendToPrinter
		self.printqueue.grid(row=0,column=1, sticky = E)

		self.updownframe = Frame(self, height = 50, width = 50)
		self.updownframe.grid(row=1,column=1, sticky = E)

		self.addqueue = Button(self)
		self.addqueue["text"] = "Add to Queue",
		self.addqueue["command"] = self.AddToQueue
		self.addqueue.grid(row=0,column=2, sticky = E)

		self.removequeue = Button(self)
		self.removequeue["text"] = "Remove From Queue",
		self.removequeue["command"] = self.RemoveFromQueue
		self.removequeue.grid(row=0,column=3, sticky = E)  

		self.connectprinter = Button(self)
		self.connectprinter["text"] = "Connect Printer",
		self.connectprinter["command"] = self.ConnectToPrinter
		self.connectprinter.grid(row=0,column=0, sticky = E)

		self.moveup = Button(self.updownframe)
		self.moveup["text"] = u'\u25b2'
		self.moveup["command"] = self.MoveUp
		self.moveup.grid(row=1,column=2, sticky = E)

		self.movedown = Button(self.updownframe)
		self.movedown["text"] = u'\u25bc'
		self.movedown["command"] = self.MoveDown
		self.movedown.grid(row=2,column=2, sticky = E)

		self.QueueList = Listbox(self)
		self.QueueList.grid(row=1,column=0, sticky = S, columnspan = 2, pady = 10)

  
	def __init__(self, master=None):
		self.CompareList = []
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()
		self.LoopDir()

 
root = Tk()
entry = Entry()
def handle(event):
	event.widget.insert(0, event.data)


app = Application(master=root)
app.mainloop()
try:
	root.destroy()
except:
	print ("closed")



