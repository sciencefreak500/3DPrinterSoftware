#! /usr/bin/env python
#This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, #You can obtain one at https://mozilla.org/MPL/2.0/
####### IMPORTS #######

import os
import pickle
import tkFileDialog as filedialog
from Tkinter import *
import shutil
import re
import subprocess
import PrinterRainbowTable
import sys

####### SCRIPT VARIABLES #######

CurrentQueue = []
ArchivedQueue = []

####### FUNCTIONS #######

def SaveState():
	global CurrentQueue
	global ArchivedQueue
	with open('setup.inf','w') as f:
		pickle.dump([CurrentQueue, ArchivedQueue], f)


def InitializeProgram():  #If first time running, set location, else pull from setup.inf
	global DirLoc;
	try:
		with open('setup.inf') as f:
			DirLoc = pickle.load(f)
                        global Dirloc
			print (Dirloc)
	except:
			root = Tk()
			DirLoc = filedialog.askdirectory(initialdir='.')
			root.destroy()
			with open('setup.inf','w') as f:
				pickle.dump([DirLoc], f)

def GetUSB():
	device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
	if os.name == 'nt':
		#df = subprocess.check_output("lsusb", shell=True) windows equivelent
		pass
	else:
		df = subprocess.check_output("lsusb", shell=True)
	devices = []
	for i in df.split('\n'):
		if i:
			info = device_re.match(i)
			if info:
				dinfo = info.groupdict()
				dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
				devices.append(dinfo) 
	ID=PrinterRainbowTable.Device()
	DeviceName=PrinterRainbowTable.DeviceName()
	n=int(0)
	found=int(1)
	Printer=[0,1,2,3,4,5,6]
	while int(len(devices)-1)>=n:
		dID=devices[n]
		m=int(0)
		while int(len(ID)-1)>=m:
			if dID['id']==ID[m]:
				Printer[found]=DeviceName[m]
				found+=1
				Printer[found]=dID['device'] #CDH needs to be changed to an append
				found+=1
			if int(len(devices)-1)==n and int(len(devices)-1)==m and found==int(0):
				Printer="null"
			m+=1
		n+=1
	Printer[0]=int(found)
	return Printer #this is the path to the printer

####### MAIN SCRIPT #######


InitializeProgram()


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
		filepath = filedialog.askopenfilename()
		n=int(0)
		revfilepath=filepath[::-1]
		while n<int(len(filepath)):
			if str(revfilepath[n])=="/":
				n=int(len(filepath)-n)
				break
			else:
				n+=1
		filename=filepath[n:len(filepath)]
		self.QueueList.insert(END,filename)
		print (filename)
		with open(os.path.join(DirLoc,filename), "w") as file1:
			toFile = raw_input("Write what you want into the field:") #CDH This is where user puts in how they want their file printed Tk()
			file1.write(toFile)
		try:
			with open('setup.inf') as f:
				CurrentQueue, ArchivedQueue = pickle.load(f)
				print (CurrentQueue, ArchivedQueue)
		except:
			file = open('setup.inf','w')
			file.close()

	def RemoveFromQueue(self):
		index = self.QueueList.index(ACTIVE)
		self.QueueList.delete(index)

	def MakeNormal(self):
		root.wm_state('normal')

	def PushBackground(self):
		print ("minimizing")
		root.wm_state('withdrawn')
		self.after(5000,self.MakeNormal)

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
		global CurrentQueue
		printList = CurrentQueue
		if printList != self.CompareList:
			try:
				if len(printList) > len(self.CompareList):  ##something needs to be added
					temp = list(set(printList) - set(self.CompareList))
					for i in temp:
						self.QueueList.insert(END,i)

				elif len(printList) < len(self.CompareList):   ##something needs to be removed
					temp = list(set(self.CompareList) - set(printList))
					for i in temp:
						gone = self.CompareList.index(i)
						self.QueueList.delete(gone)
				elif set(printList) == set(self.CompareList):
					pass
				else:   ##Something bad happened, reset list
					self.QueueList.delete(0, END)
					for i in printList:
						self.QueueList.insert(END,i)
			except:
				print ("something wrong")

		currentQueue = list(self.QueueList.get(0,END))

		self.CompareList = self.QueueList.get(0,END)
		self.after(1000, self.LoopDir)

	def createWidgets(self):
		self.background = Button(self)
		self.background["text"] = "Push To Background",
		self.background["command"] = self.PushBackground
		self.background.grid(row=0,column=0, sticky = W)

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
		self.connectprinter.grid(row=1,column=2, sticky = E)

		self.moveup = Button(self.updownframe)
		self.moveup["text"] = u'\u25b2'
		self.moveup["command"] = self.MoveUp
		self.moveup.grid(row=1,column=1, sticky = E)

		self.movedown = Button(self.updownframe)
		self.movedown["text"] = u'\u25bc'
		self.movedown["command"] = self.MoveDown
		self.movedown.grid(row=2,column=1, sticky = E)

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
	SaveState()
	print ("closed")
