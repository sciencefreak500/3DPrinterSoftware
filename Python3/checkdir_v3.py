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
import MultiPrinterMenuOptionCreator
import PrintProgramUI as gui

####### SCRIPT VARIABLES #######




CurrentQueue = []


firstRun="0"

#Add on to the devices by adding to the list in the categories. make sure the element index is the same
Printers = {
        'DeviceName':["Ultimaker2","Bukito","Red Wheel Mouse"],
        'ID': ["2341:0042","16c0:0483","04b3:310b"]
        }


####### FUNCTIONS #######

def SaveState():
    global CurrentQueue
    with open('setup.inf','wb') as f:
        pickle.dump([CurrentQueue], f)
    print("saved")


def InitializeProgram():
    global CurrentQueue
    try:
        with open('setup.inf','rb') as f:
            CurrentQueue = pickle.load(f)
    except:
            file = open('setup.inf','wb')
            file.close()

    print (CurrentQueue)
   
    
                
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




def loadList():
    print (CurrentQueue)
    for i in CurrentQueue:
        #ui.PrintQueue.addItem(window,temp)
        pass
        
            
        
    
    #add CurrentQueue to GUI list
    #for i in CurrentQueue:
    #    self.QueueList.insert(END,i['Name'])

def AddToQueue():
    filepath = gui.QtGui.QFileDialog.getOpenFileName(window,'Select file to Add')
    fileName = filepath.split('/')[-1]
    ##
    #other questions to get further info about file (times to print, time, etc)
    ##
    tempdict = {'Name': fileName, 'Path': filepath}
    CurrentQueue.append(tempdict)
    print("Added")
    #add to GUI list (at end)
    #self.QueueList.insert(END,fileName)
    SaveState()

def RemoveFromQueue():
    #get active in GUI list, then delete it
    #index = self.QueueList.index(ACTIVE)
    #self.QueueList.delete(index)
    print("deleted")
    #CurrentQueue[index] = None
    #CurrentQueue.remove(None)
    #SaveState()
    print(CurrentQueue)

def MakeNormal():
    print("return to normal")
    #root.wm_state('normal')

def PushBackground():
    print ("minimizing")
    #root.wm_state('withdrawn')
    #self.after(5000,self.MakeNormal)

def SendToPrinter():
    print ("functionality")

def MoveUp():
    print('moved up')
    #a = CurrentQueue[pos]
    #b = CurrentQueue[pos-1]
    #CurrentQueue[pos] = b
    #CurrentQueue[pos-1] = a
    SaveState()
    #wipe GUI list, repopulate
    #print(CurrentQueue)

def MoveDown():
    print('moved down')
    #a = CurrentQueue[pos]
    #b = CurrentQueue[pos+1]
    #CurrentQueue[pos] = b
    #CurrentQueue[pos+1] = a
    SaveState()
    #wipe GUI list, repopulate
    #print(CurrentQueue)

'''
#pyusb should be working. Will test this.
 #once again, going to need to find another lib for this.
def ConnectToPrinter():
    global firstRun
    if firstRun=="0":
        PortsnNames=GetUSB()
        Ports=PortsnNames[0]
        Names=PortsnNames[1]
        with open('setup.inf','wb') as f:
                pickle.dump([Names], f)
        MultiPrinterMenuOptionCreator.Main()
        with open('setup.inf','rb') as f:
            Printers=pickle.load(f)
        if Names==[]:
            self.connectPrinterLabel.set("No Printer was Found")
        else:
            firstRun="1"
            conPrinters=[]
            conPorts=[]
            n=0
            while n<len(Names):
                if str(Printers[n])=="['1']":
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
        self.connectPrinterText.set("Connect Printer")
        self.connectPrinterLabel.set("")

'''
  
def ExitApp():
    sys.exit(app.exec_())

def FunctionGuiMap():
    ui.UpButton.clicked.connect(MoveUp)
    ui.DownButton.clicked.connect(MoveDown)
    ui.actionPrint.triggered.connect(SendToPrinter)
    ui.actionExit.triggered.connect(ExitApp)
    ui.actionAdd_To_Queue.triggered.connect(AddToQueue)
    ui.actionRemove_from_Queue.triggered.connect(RemoveFromQueue)

    loadList()


    

if __name__ == "__main__":
    app = gui.QtGui.QApplication(sys.argv)
    window = gui.QtGui.QMainWindow()
    ui = gui.Ui_window()
    ui.setupUi(window)
    FunctionGuiMap()
    window.show()
    sys.exit(app.exec_())




'''
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
'''
