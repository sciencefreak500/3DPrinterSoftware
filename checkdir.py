#! /usr/bin/env python
####### IMPORTS #######

import os
import pickle
import tkFileDialog as filedialog
from Tkinter import *
import shutil

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



####### MAIN SCRIPT #######


InitializeProgram()

class Application(Frame):
    
    def MakeNormal(self):
        root.wm_state('normal')
        
    def PushBackground(self):
        print "minimizing"
        root.wm_state('withdrawn')
        self.after(5000,self.MakeNormal)

    def SendToPrinter(self):
	printer=/path/to/printer #this will have to grab the path from the settings that the User enters to connect to the printer
        File=str(DirLoc+checkdir.Queue1)
        shutil.move(DirLoc+File, printer) #need to find out how printer processes files to send them over correctly
	os.remove(DirLoc+File)

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

        self.background = Button(self)
        self.background["text"] = "Send to Printer",
        self.background["command"] = self.SendToPrinter
        self.background.grid(row=0,column=1, sticky = E)

        self.background = Button(self)
        self.background["text"] = "Move Up Queue",
        self.background["command"] = self.MoveUp
        self.background.grid(row=2,column=1, sticky = E)

        self.background = Button(self)
        self.background["text"] = "Move Down Queue",
        self.background["command"] = self.MoveDown
        self.background.grid(row=2,column=2, sticky = E)

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






