####### IMPORTS #######

import os
import pickle
import tkFileDialog as filedialog
from Tkinter import *
import shutil
os.environ['TKDND_LIBRARY'] = 'TKDND_DIR'
from tkdnd_wrapper import TkDND


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
            print FilesInDirectory
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

    def SendToFolder(self):
        filename = filedialog.askopenfilename()
        shutil.copy(filename,DirLocation)

    def LoopDir(self):
        PrintList = CheckDirChanges()
        #self.QueueList.insert
        self.after(1000, self.LoopDir)

    def createWidgets(self):
        self.background = Button(self)
        self.background["text"] = "Push To Background",
        self.background["command"] = self.PushBackground
        self.background.grid(row=0,column=0, sticky = W)

        self.background = Button(self)
        self.background["text"] = "Send to Printer",
        self.background["command"] = self.SendToFolder
        self.background.grid(row=0,column=1, sticky = E)

        self.QueueList = Listbox(self)
        self.QueueList.grid(row=1,column=0, sticky = S, columnspan = 2, pady = 10)
        

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        
        self.createWidgets()
        self.LoopDir()
        
        
        

root = Tk()
dnd = TkDND(root)

entry = Entry()
def handle(event):
    event.widget.insert(0, event.data)

dnd.bindtarget(entry, handle, 'text/uri-list')

app = Application(master=root)
app.mainloop()
try:
    root.destroy()
except:
    print "closed"



