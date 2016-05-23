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

####### SCRIPT VARIABLES #######

DirLocation = ''

####### FUNCTIONS #######

def SetFirstRun():  #refresh setup.inf as if first run
    FirstRun = True
    DirLoc = ''
    with open('setup.inf','w') as f:
        pickle.dump([FirstRun, DirLoc], f)
    InitializeProgram()


def InitializeProgram():  #If first time running, set location, else pull from setup.inf
    global DirLocation;
    try:
        with open('setup.inf') as f:
            FirstRun, DirLoc = pickle.load(f)
        if FirstRun == True:
            root = Tk()
            DirLocation = filedialog.askdirectory(initialdir='.')
            root.destroy()
            FirstRun = False
            DirLoc = DirLocation
            with open('setup.inf','w') as f:
                pickle.dump([FirstRun, DirLoc], f)
        else:
            DirLocation = DirLoc
            print DirLoc
    except:
        file = open('setup.inf','w')
        file.close()
        SetFirstRun()
        
def CheckDirChanges(): #check directory is empty, else print files/folders listed
    try:
        FilesInDirectory = os.listdir(DirLocation)
        if FilesInDirectory == []:
            print "empty"
            FilesInDirectory
        else:
            return FilesInDirectory
            
    except OSError as ex:
        print ex.errno
        print "The dir ain't there! Makin' it!"
        try:
            patharray = DirLocation.split('/')
            dirname = patharray[-1]
            os.mkdir(dirname)
        except:
            SetFirstRun()


def GetUSB():
    device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
    if os.name == 'nt':
        #df = subprocess.check_output("lsusb", shell=True) windows equivelent
	pass #pass is a place holder until bug is fixed
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
    m=int(2) #this value needs to be user inputed
    n=int(0)
    ID=PrinterRainbowTable.Device()
    found=int(0)
    while int(len(devices)-1)>=n:
		dID=devices[n]
		if dID['id']==ID[m]:
			print "Printer found, functionality."
			found=int(1)
			break
		if int(len(devices)-1)==n and found!=int(1):
			print "Printer not found."
		n+=1
    print dID['device'] #this is the path to the printer
    #with open(dID['device'],"rb") as f:
    #    data=f.read()
    #    printerbinary=data.encode('ascii')
    #print printerbinary  #CDH How do you work with pure binary data in pyhton?
####### MAIN SCRIPT #######

InitializeProgram()
   

class Application(Frame):
    def ConnectToPrinter(self):
		GetUSB()

    def AddToQueue(self):
                File = filedialog.askdirectory(initialdir='.')
    
    def MakeNormal(self):
        root.wm_state('normal')
        
    def PushBackground(self):
        print "minimizing"
        root.wm_state('withdrawn')
        self.after(5000,self.MakeNormal)

    def SendToPrinter(self):
        print "functionality"
        '''
<<<<<<< HEAD
        File=str(DirLoc+checkdir.Queue1)
        shutil.move(DirLoc+File, Printer) #need to find out how printer processes files to send them over correctly
	os.remove(DirLoc+File)
=======
        filename = filedialog.askopenfilename()
        try:
            shutil.copy(filename,DirLocation)
        except:
            print "User closed before selecting"

>>>>>>> 6dcd4e4d741c503dd4722eaa9f38c7e7c063ee41
        '''
    def MoveUp(self):
        l = self.QueueList
        try:    
            pos = list(l.curselection())[0]
        except:
            return
        if pos == 0:
            print "is zero"
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
            print "is end"
            return
        text = l.get(pos)
        l.delete(pos)
        l.insert(pos+1, text)
        l.selection_set(pos+1)
        

    def LoopDir(self):
        PrintList = CheckDirChanges()
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
                        self.QueueList.delete(gone,gone)

                elif set(PrintList) == set(self.CompareList):
                    pass
                        
                else:   ##Something bad happened, reset list
                    self.QueueList.delete(0, END)
                    for i in PrintList:
                        self.QueueList.insert(END,i)
            except:
                print "something wrong"

        
        self.CompareList = self.QueueList.get(0,END)
        self.after(1000, self.LoopDir)

    def createWidgets(self):
        self.background = Button(self)
        self.background["text"] = "Push To Background",
        self.background["command"] = self.PushBackground
        self.background.grid(row=0,column=0, sticky = W)

        self.sendqueue = Button(self)
        self.sendqueue["text"] = "Print Queue",
        self.sendqueue["command"] = self.SendToPrinter
        self.sendqueue.grid(row=0,column=1, sticky = E)

        self.updownframe = Frame(self, height = 50, width = 50)
        self.updownframe.grid(row=1,column=1, sticky = E)

        self.sendqueue = Button(self)
        self.sendqueue["text"] = "Add to Queue",
        self.sendqueue["command"] = self.AddToQueue
        self.sendqueue.grid(row=0,column=2, sticky = E)        

        self.sendqueue = Button(self)
        self.sendqueue["text"] = "Connect Printer",
        self.sendqueue["command"] = self.ConnectToPrinter
        self.sendqueue.grid(row=1,column=2, sticky = E)

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
    print "closed"

