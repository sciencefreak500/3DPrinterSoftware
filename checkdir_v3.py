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
import ConnectPrinterMenuOptionCreator
import AddQueueMenuCreator

####### SCRIPT VARIABLES #######

CurrentQueue = []
ArchivedQueue = []

firstRun="0"
sending="0"
conPrinters=[]

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


def InitializeProgram():
    global CurrentQueue
    global ArchivedQueue
    try:
        with open('setup.inf','rb') as f:
            CurrentQueue, ArchivedQueue = pickle.load(f)
    except:
            file = open('setup.inf','wb')
            file.close()
    
                
#going to need to find another lib for this one, something cross platform
def GetUSB():
	global Printers
	if sys.platform == 'win32':
		#df = subprocess.check_output("lsusb", shell=True) needs windows equivelent
		pass
	elif sys.platform == 'darwin': #df = subprocess.check_output("lsusb", shell=True) mac equivelent is system_profiler SPUSBDataType to raplce lsusb
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
	            subUSBInfo=USBInfo[n]
	            if subUSBInfo[2:11]==ID[m]: 
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
        for i in CurrentQueue:
            x=i[0]
            y=str(str(x['Name'])+" "*5+str(x['Printers'])+" "*5+str(x['Number']))
            self.QueueList.insert(END,y)

    def AddToQueue(self):
        with open('setup.inf','wb') as f:
                    pickle.dump([conPrinters], f)
        AddQueueMenuCreator.Main()
        with open('setup.inf','rb') as f:
                QueueAddition=pickle.load(f)
        if str(QueueAddition)!="[[]]":
                CurrentQueue.append(QueueAddition)
                x=QueueAddition[0]
                y=str(str(x['Name'])+" "*5+str(x['Printers'])+" "*5+str(x['Number']))
                self.QueueList.insert(END,y)
                SaveState()
    
    def RemoveFromQueue(self):
        index = self.QueueList.index(ACTIVE)
        self.QueueList.delete(index)
        CurrentQueue[index] = None
        CurrentQueue.remove(None)
        SaveState()

    def MakeNormal(self):
        root.wm_state('normal')

    def PushBackground(self):
        print ("minimizing")
        root.wm_state('withdrawn')
        self.after(5000,self.MakeNormal)

    def SendToPrinter(self):
        global CurrentQueue
        global sending
        if sending=="0":
            sending="1"
            self.QueueList.itemconfig(0,{'bg':'yellow'})
            print(CurrentQueue)
            i=CurrentQueue[0]
            x=i[0]
            z=int(x['Number'])-1
            y=str(str(x['Name'])+" "*5+str(x['Printers'])+" "*5+str(z))
            i[0]=y
            CurrentQueue=[i]
            print(CurrentQueue)
            #    self.QueueList.insert(END,y)
        else:
            sending="0"
            self.QueueList.itemconfig(0,{'bg':'white'})
            print("pause queue")

    def MoveUp(self):
        l = self.QueueList
        try:
            pos = list(l.curselection())[0]
        except:
            return
        if pos == 0:
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

    def MoveDown(self):
        l = self.QueueList
        try:
            pos = list(l.curselection())[0]
        except:
            return
        if pos == len(l.get(0, END))-1:
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


     #once again, going to need to find another lib for this.
    def ConnectToPrinter(self):
        global firstRun
        if firstRun=="0":
            PortsnNames=GetUSB()
            Ports=PortsnNames[0]
            Names=PortsnNames[1]
            with open('setup.inf','wb') as f:
                    pickle.dump([Names], f)
            ConnectPrinterMenuOptionCreator.Main()
            with open('setup.inf','rb') as f:
                Printers=pickle.load(f)
            if Names==[]:
                self.connectPrinterLabel.set("No Printer was Found")
            else:
                firstRun="1"
                conPorts=[]
                Printers=Printers[0]
                n=0
                while n<len(Names):
                    global conPrinters
                    print(Printers)
                    if str(Printers[n])=='1':
                        conPrinters.append(Names[n])
                        conPorts.append(Ports[n])
                    n+=1
                if str(conPorts)=='[]':
                    self.connectPrinterLabel.set("No Printer was Selected")
                    firstRun="0"
                else:
                    self.connectPrinterText.set("Disconnect Printer")
                    self.connectPrinterLabel.set("Connected to "+str(conPrinters))
            n=0
            while n<len(conPorts) and conPorts[0]!='[]':
                with open(conPorts[n],"rb") as f:
                    data=f.read()
                print (data) 
                n+=1 
        else:
            print("pause queue") 
            firstRun="0"
            conPrinters=[]
            conPorts=[]
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
        self.QueueList.grid(row=1,column=0, columnspan = 2, pady = 10)

        self.printingLabel=StringVar()
        self.printinglabel=Label(self,textvariable=self.printingLabel)
        self.printinglabel.grid(row=2,column=2, sticky = E)
  
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
