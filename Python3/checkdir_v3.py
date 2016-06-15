#! /usr/bin/env python3
#This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, #You can obtain one at https://mozilla.org/MPL/2.0/

'''
--------------------DESCRIPTION----------------------------
checkdir_v3.py is the newer version using Python3 where 
files are located on the computer, their location and filename 
is stored in the list, and you can modify this array as you see fit.
'''



####### IMPORTS #######

from tkinter import filedialog
from tkinter import *
import subprocess
import sys
import pickle

####### SCRIPT VARIABLES #######

CurrentQueue = []
ArchivedQueue = []

firstRun="0"

#Add on to the devices by adding to the list in the categories. make sure the element index is the same
Printers = {
        'DeviceName':["Ultimaker2","Bukito","Red Wheel Mouse"],
        'ID': ["2341:0042","16c0:0483","04b3:310b"]
        }



####### FUNCTIONS #######

def SaveState():
    global CurrentQueue
    global ArchivedQueue
    with open('setup.inf','wb') as f:
        pickle.dump([CurrentQueue, ArchivedQueue], f)
    print("saved")


def InitializeProgram():  #If first time running, set location, else pull from setup.inf
    global CurrentQueue
    global ArchivedQueue
    try:
        with open('setup.inf','rb') as f:
            CurrentQueue, ArchivedQueue = pickle.load(f)
    except:
            file = open('setup.inf','wb')
            file.close()

    print (CurrentQueue)
    print (ArchivedQueue)
    
                
#going to need to find another lib for this one, something cross platform
def GetUSB():
	global Printers
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
	ID=Printers['ID'] 
	DeviceName=Printers['DeviceName']
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


InitializeProgram()


class Application(Frame):

    def loadList(self):
        print (CurrentQueue)
        for i in CurrentQueue:
            self.QueueList.insert(END,i['Name'])

    def AddToQueue(self):
        filepath = filedialog.askopenfilename()
        fileName = filepath.split('/')[-1]
        ##
        #other questions to get further info about file (times to print, time, etc)
        ##
        tempdict = {'Name': fileName, 'Path': filepath}
        CurrentQueue.append(tempdict)
        self.QueueList.insert(END,fileName)
        SaveState()
    
    def RemoveFromQueue(self):
        index = self.QueueList.index(ACTIVE)
        self.QueueList.delete(index)
        CurrentQueue[index] = None
        CurrentQueue.remove(None)
        SaveState()
        print(CurrentQueue)

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

        a = CurrentQueue[pos]
        b = CurrentQueue[pos-1]
        CurrentQueue[pos] = b
        CurrentQueue[pos-1] = a
        SaveState()
        print(CurrentQueue)

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

        a = CurrentQueue[pos]
        b = CurrentQueue[pos+1]
        CurrentQueue[pos] = b
        CurrentQueue[pos+1] = a
        SaveState()
        print(CurrentQueue)


     #once again, going to need to find another lib for this.
    def ConnectToPrinter(self):
        global firstRun
        if firstRun=="0":
            PortsnNames=GetUSB()
            Ports=PortsnNames[0]
            Names=PortsnNames[1]
            if Ports== []:
                self.connectPrinterLabel.set("No Printer was Found")#Needs to be changed to pop up menu asking if this is an error and to start enacting secondary method of connection.
            elif len(Ports)==1:
                firstRun="1"
                self.connectPrinterText.set("Disconnect Printer")
                self.connectPrinterLabel.set("Connected to "+str(Names))
            else:
                firstRun="1"
                Name="GUI needs to be created to select which printer to connect to in case of multiple printers found."	#GUI needs to be created to select which printer to connect to in case of multiple printers found.
                print(Name)
                self.connectPrinterText.set("Disconnect Printer")
                self.connectPrinterLabel.set("Connected to "+str(Name))
			#with open(port,"rb") as f:
				#	data=f.read()
				#	printerbinary=data.encode('ascii')
				#print printerbinary  #CDH How do you work with pure binary data in pyhton?
        else:
            print("pause queue") 
            firstRun="0"
            self.connectPrinterText.set("Connect Printer")
            self.connectPrinterLabel.set("")


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

        self.connectPrinterLabel=StringVar()
        self.connectprinterlabel=Label(self,textvariable=self.connectPrinterLabel)
        self.connectprinterlabel.grid(row=2,column=2, sticky = E)
	
        self.connectPrinterText=StringVar()
        self.connectPrinterText.set("Connect Printer")
        self.connectprinter = Button(self)
        self.connectprinter["textvariable"] = self.connectPrinterText,
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
        self.loadList()

 
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

