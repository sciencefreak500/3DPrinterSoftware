#! /usr/bin/env python3
#This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, #You can obtain one at https://mozilla.org/MPL/2.0/
####### IMPORTS #######

from tkinter import *
from tkinter import filedialog
import subprocess
import sys
import importlib
import Setup
import PrinterRainbowTable
import PrinterQueue

####### SETUP ######
with open("Setup.py", "w") as f:
	f.write("""#! /usr/bin/env python3
#This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, #You can obtain one at https://mozilla.org/MPL/2.0/

def N():
	n="0"
	return n""")
importlib.reload(Setup)
####### FUNCTIONS #######	

def WriteToQueue():
	print("Pop up menu for user to enter print settings")
	importlib.reload(PrinterQueue)
	currentFileName=PrinterQueue.CurrentFileName()
	currentFilePath=PrinterQueue.CurrentFilePath()
	currentPrintNumber=PrinterQueue.CurrentPrintNumber()
	currentPrintType=PrinterQueue.CurrentPrintType()
	filePath = filedialog.askopenfilename()
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
""")
	importlib.reload(PrinterQueue)

def DeleteFromQueue(fileName):
	importlib.reload(PrinterQueue)
	currentFileName=PrinterQueue.CurrentFileName()
	currentFilePath=PrinterQueue.CurrentFilePath()
	currentPrintNumber=PrinterQueue.CurrentPrintNumber()
	currentPrintType=PrinterQueue.CurrentPrintType()
	index=currentFileName.index(fileName)
	currentFileName.pop(index)
	currentFilePath.pop(index)
	#currentFilePrintNumber.pop(index)
	#currentFilePrintType.pop(index)
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
""")
	importlib.reload(PrinterQueue)

def GetUSB():
	if sys.platform == 'win32':
		#df = subprocess.check_output("lsusb", shell=True) needs windows equivelent
		pass
	elif sys.platform == 'darwin': #df = subprocess.check_output("lsusb", shell=True) needs mac equivelent
		pass
	else:
		USB = subprocess.check_output("lsusb", shell=True)
	USBInfo= []
	for i in USB.split():
		USBInfo.append(str(i))
	Ports= []
	Names= []
	ID=PrinterRainbowTable.Device()
	DeviceName=PrinterRainbowTable.DeviceName()
	n=int(0)
	while int(len(USBInfo)-1)>=n:
		m=int(0)
		while int(len(ID)-1)>=m:
			if USBInfo[n]==ID[m]: 
				bus=USBInfo[int(n-4)]
				device=USBInfo[int(n-2)]
				Path=str("/dev/bus/usb/"+bus[2:5]+"/"+device[2:5])
				Ports.append(Path)
				Names.append(DeviceName[m])
			m+=1
		n+=1
	PortsnNames=[Ports,Names]
	return PortsnNames #this is the path to the printer
####### MAIN SCRIPT #######


class Application(Frame):
	def ConnectToPrinter(self):
		n=Setup.N()
		if n=="0":
			PortsnNames=GetUSB()
			Ports=PortsnNames[0]
			Names=PortsnNames[1]
			if Ports== []: #Weather the printer is connected or not needs to be displayed in the GUI
				self.connectPrinterLabel.set("No Printer was Found")
			elif len(Ports)==1:
				with open("Setup.py", "w") as f:
					f.write("""#! /usr/bin/env python3
#This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, #You can obtain one at https://mozilla.org/MPL/2.0/

def N():
	n="1"
	return n""")
				importlib.reload(Setup)
				self.connectPrinterText.set("Disconnect Printer")
				self.connectPrinterLabel.set("Connected to "+str(Names))
			else:
				with open("Setup.py", "w") as f:
					f.write("""#! /usr/bin/env python3
#This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, #You can obtain one at https://mozilla.org/MPL/2.0/

def N():
	n="1"
	return n""")
				importlib.reload(Setup)
				self.connectPrinterText.set("Disconnect Printer")
				Name="GUI needs to be created to select which printer to connect to in case of multiple printers found."	#GUI needs to be created to select which printer to connect to in case of multiple printers found.
				self.connectPrinterLabel.set("Connected to "+str(Name))
			#with open(port,"rb") as f:
				#	data=f.read()
				#	printerbinary=data.encode('ascii')
				#print printerbinary  #CDH How do you work with pure binary data in pyhton?
		else:
			print("pause queue")
			with open("Setup.py", "w") as f:
				f.write("""#! /usr/bin/env python3
#This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, #You can obtain one at https://mozilla.org/MPL/2.0/

def N():
	n="0"
	return n""")
			importlib.reload(Setup)
			self.connectPrinterText.set("Connect Printer")
			self.connectPrinterLabel.set("")

	def AddToQueue(self):	
		WriteToQueue()
		fileName=PrinterQueue.CurrentFileName()
		fileName=fileName[int(len(fileName)-1)]
		self.QueueList.insert(END,fileName)
		

	def RemoveFromQueue(self):
		index = self.QueueList.index(ACTIVE)
		fileName=PrinterQueue.CurrentFileName()
		fileName=fileName[index]
		DeleteFromQueue(fileName)
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
			print ("is beggining")
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
		self.QueueList.delete(0, END)
		fileName=PrinterQueue.CurrentFileName()
		for i in fileName:
			self.QueueList.insert(END,i)	
		self.after(10000, self.LoopDir) #active value needs to be cataglogged so that it isn't lost when LoopDir resets

	def createWidgets(self):

		self.printqueue = Button(self)
		self.printqueue["text"] = "Print Queue",
		self.printqueue["command"] = self.SendToPrinter
		self.printqueue.grid(row=0,column=1, sticky = E)

		self.updownframe = Frame(self, height = 50, width = 50)
		self.updownframe.grid(row=2,column=1, sticky = E)

		self.addqueue = Button(self)
		self.addqueue["text"] = "Add to Queue",
		self.addqueue["command"] = self.AddToQueue
		self.addqueue.grid(row=0,column=2, sticky = E)

		self.removequeue = Button(self)
		self.removequeue["text"] = "Remove From Queue",
		self.removequeue["command"] = self.RemoveFromQueue
		self.removequeue.grid(row=0,column=3, sticky = E)  

		self.connectPrinterText=StringVar()
		self.connectPrinterText.set("Connect Printer")
		self.connectprinter = Button(self)
		self.connectprinter["textvariable"] = self.connectPrinterText,
		self.connectprinter["command"] = self.ConnectToPrinter
		self.connectprinter.grid(row=0,column=0, sticky = E)
		
		self.connectPrinterLabel=StringVar()
		self.connectprinterlabel=Label(self,textvariable=self.connectPrinterLabel)
		self.connectprinterlabel.grid(row=1,column=0, sticky = E)	

		self.moveup = Button(self.updownframe)
		self.moveup["text"] = u'\u25b2'
		self.moveup["command"] = self.MoveUp
		self.moveup.grid(row=2,column=2, sticky = E)

		self.movedown = Button(self.updownframe)
		self.movedown["text"] = u'\u25bc'
		self.movedown["command"] = self.MoveDown
		self.movedown.grid(row=3,column=2, sticky = E)

		self.QueueList = Listbox(self,xscrollcommand=True,yscrollcommand=True)
		self.QueueList.grid(row=2,column=0, sticky = S, columnspan = 2, pady = 10)
		self.LoopDir()

  
	def __init__(self, master=None):
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
