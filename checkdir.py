####### IMPORTS #######

import os.path
import pickle
import tkFileDialog as filedialog
from Tkinter import *


####### SCRIPT VARIABLES #######

DirLocation = ''


####### FUNCTIONS #######

def SetFirstRun():  #refresh setup.inf as if first run
    FirstRun = True
    DirLoc = ''
    with open('setup.inf','w') as f:
        pickle.dump([FirstRun, DirLoc], f)


def InitializeProgram():  #If first time running, set location, else pull from setup.inf
    global DirLocation;
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

        
        
def CheckDirChanges(): #check directory is empty, else print files/folders listed
    try:
        FilesInDirectory = os.listdir(DirLocation)
        if FilesInDirectory == []:
            print "empty"
        else:
            print FilesInDirectory
            
    except OSError as ex:
        print ex.errno



####### MAIN SCRIPT #######
        
#SetFirstRun()
InitializeProgram()
CheckDirChanges()
