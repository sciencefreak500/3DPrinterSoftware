#! /usr/bin/env python3
#This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, #You can obtain one at https://mozilla.org/MPL/2.0/

'''
--------------------DESCRIPTION----------------------------
checkdir_v3.py is the newer version using Python3 where 
files are located on the computer, their location and filename 
is stored in the list, and you can modify this array as you see fit.
'''



'''
<<<<<CHRIS>>>>>

Just a note, right now, the ConnectToPrinter function does not work because
This is what I am currently working on. You may have to pyuic4 the ConnectToPrinter.ui
file. Type this into terminal:

pyuic4 ConnectToPrinter.ui -o ConnectToPrinter.py

if it gives you trouble. Good luck! Have fun!

'''

####### IMPORTS #######


import subprocess
import sys
import pickle

import os.path
import PrintProgramUI as gui
import AddToQueue as queueDialog
import ConnectToPrinter as connectDialog
## non-native ##

import serial
import serial.tools.list_ports as listports

####### SCRIPT VARIABLES #######

CurrentQueue = []

# CurrentQueue structure:
#		 Device Name, Number of prints, [list of printers connected]

#its better to use bool than int. True/False 
firstRun = False
sending = False
conPrinters = []
filepath = ""
printnumbers = ""


#Add on to the devices by adding to the list in the categories. make sure the element index is the same, the devide and vendor id's are in decimal
Printers = {'DeviceName':["Ultimaker2","Bukito"],
            'Shortname': ["Ult2","Buk"],
            'ID': ["2341:0042","5824:1155",]
			}


####### FUNCTIONS #######

def SaveState():
    global CurrentQueue
    with open('setup.inf','wb') as f:
        pickle.dump([CurrentQueue], f)


def InitializeProgram():
    global CurrentQueue
    try:
        with open('setup.inf','rb') as f:
            CurrentQueue = pickle.load(f)
            print (CurrentQueue)
    except:
            file = open('setup.inf','wb')
            file.close()
    
                
# gets devices from pyserial by vidpid, pumps to ConnectToPrinter 
def GetUSB():
        global Printers
        Ports = []
        Names = []
        DeviceName = Printers['DeviceName']
        ID = Printers['ID']
        device = listports.comports()
        for i in device:
                vid = str(i.vid)
                pid = str(i.pid)
                PortID = vid + ":" + pid
                for n, x in enumerate(ID):
                        if x == PortID:
                                Path = str(i.device)
                                Ports.append(Path)
                                Names.append(DeviceName[n])
        return Ports, Names #this is the path to the printer
		#sends out comports, and Names in PortsnNames



def loadList(self):
    for i in CurrentQueue:
        x = i[0]
        y = str(str(x['Name'])+" " * 5 + str(x['Printers']) + " " * 5 +str(x['Number']))
        



    
def RemoveFromQueue():
    print("remove from queue")
    #index = self.QueueList.index(ACTIVE)
    #self.QueueList.delete(index)
    #CurrentQueue[index] = None
    #CurrentQueue.remove(None)
    SaveState()
	
	
#THE ACUAL PRINT FUNCTION
def SendToPrinter(self):
    global CurrentQueue
    global sending
    if sending == False:
        sending = True
        #self.printqueueText.set("Stop Printing Queue")
        while str(CurrentQueue)!='[]':
            sub = CurrentQueue[0]
            x = sub[0]
            while 0 < x['Number']:
                #while loop is for counting for number of prints - backwards
                x['Number'] = int(x['Number']) - 1
                sub[0] = x
                CurrentQueue[0] = sub
                self.QueueList.delete(0)
                if x['Number']>0:
                    y = str(str(x['Name'])+" " * 5 + str(x['Printers']) + " " * 5 + str(x['Number']))  #format for tkinter
                    self.QueueList.insert(0,y)
                    gfile = open(x['Path'])
					#actual connection to serial below
                    ser = serial.Serial(conPorts[0],250000,timeout=1) #(port, baudrate, timeout) needs to be able to handle more than one printer, also needs to stopgrabbing program
                    print(serial.Serial.get_settings(ser))
                    print(ser.readline())
                    ser.write(b'''G92 E0
G28''')
                    for line in gfile:
                            gcode=bytes(gfile.readline(), 'utf-8')
                            ser.write(gcode)
                    print(ser.readline())  #home key
                    ser.write(b'''G92 E0
G28''')
                    ser.close()
                    gfile.close()
                    print("sweep bed")
                SaveState()
            print("passing next item")   #repeat the while loop 
            CurrentQueue.pop(0) #get rid of first item,
    else:
        sending = False
        self.printqueueText.set("Print Queue")
        self.QueueList.itemconfig(0,{'bg':'white'})  #done printing or didnt do anything
        print("pause queue")

		
def MoveUp():
    '''l = self.QueueList
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
    CurrentQueue[pos-1] = a'''
    print("move up")
    SaveState()

def MoveDown():
    '''l = self.QueueList
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
    CurrentQueue[pos+1] = a'''
    print("move down")
    SaveState()

#get printer connection
def ConPrint():
    ConnectDialog.show()
    
def ConnectToPrinter(self):
    
    global conPorts
    global firstRun
    if firstRun == False:
        Ports, Names = GetUSB()
        with open('setup.inf','wb') as f:
                pickle.dump([Names], f)
        ConnectPrinterMenuOptionCreator.Main()
        with open('setup.inf','rb') as f:
            Printers=pickle.load(f)
        if Names==[]:
            self.connectPrinterLabel.set("No Printer was Found") #no names were found in pyserial.comports
        else:
            firstRun = True
            conPorts=[]
            Printers=Printers[0]
            n= 0 
            while n<len(Names):
                global conPrinters
                if str(Printers[n])=='1':
                    conPrinters.append(Names[n])  #if connected, put this in the list of connected printers
                    conPorts.append(Ports[n])
                n+=1
            if str(conPorts)=='[]':
                self.connectPrinterLabel.set("No Printer was Selected")
                firstRun = False
            else:
                self.connectPrinterText.set("Disconnect Printer")
                self.connectPrinterLabel.set("Connected to "+str(conPrinters))
        n=0
        while n<len(conPorts) and conPorts[0]!='[]':
            ser=serial.Serial(conPorts[n],250000,timeout=1) #(port, baudrate, timeout
            print(serial.Serial.get_settings(ser))
            print(ser.readline())
            ser.write(b'''G92 E0
G28''') #Homes printer, should work for all printers
            print(ser.readline())
            ser.close()
            n+=1 
    else:
        print("pause queue") 
        firstRun = False
        conPrinters=[]
        conPorts=[]
        self.connectPrinterText.set("Connect Printer")
        self.connectPrinterLabel.set("")
'''
 
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

'''

def EndProgram():
    sys.exit(app.exec_())



def test():
    print("functionality")


def AddToQueue():
    global printnumber
    global filepath
    QueueDialog.show()
    printnumber = "1"
    QueueUI.PrintNumEdit.setText(printnumber)
    filepath = "..."
    QueueUI.lbl_FileName.setText(filepath)
    

def FileDialogBox():
    global filepath
    filepath = "..."
    filepath = queueDialog.QtGui.QFileDialog.getOpenFileName(None,"Choose File")
    if filepath == "":
        filepath = "..."
        QueueUI.lbl_FileName.setText(filepath)
    else:
        QueueUI.lbl_FileName.setText(filepath.split("/")[-1])
        print(filepath)



def CheckItemNumberEntry():
    global printnumber
    printnumber = "1"
    try:
        tempnumber = int(QueueUI.PrintNumEdit.text())
        printnumber = str(tempnumber)
    except:
        if QueueUI.PrintNumEdit.text() == "":
            pass
        else:
            msg = queueDialog.QtGui.QMessageBox()
            msg.setText("This entry should only contain numbers. Please enter print number again.")
            msg.setWindowTitle("Entry Incorrect")
            msg.exec_()
        printnumber = "1"



def VerifyAddItemEntry():
    global filepath
    global printnumber
    global CurrentQueue
    error = False
    if filepath == "...":
        error = True

    if error == True:
        msg = queueDialog.QtGui.QMessageBox()
        msg.setText("Required entries are not complete. Please correct this and try again.")
        msg.setWindowTitle("Entry Incorrect")
        msg.exec_()
        
        AddToQueue()

    else:
        #print(filepath, printnumber)
        tempdict = {'Name':filepath.split('/')[-1], 'Path':filepath, 'Number':printnumber}
        CurrentQueue.append(tempdict)
        pumpstring = tempdict['Name'] + " | " + tempdict['Number']
        ui.list_PrintQueue.addItem(pumpstring)
        

def EnableButtons():
    if ui.listPrinterList.count() == 0:
        ui.btn_MoveDown.setEnabled(False)
        ui.btn_MoveUp.setEnabled(False)
        ui.btn_Disconnect.setEnabled(False)
        ui.btn_addItem.setEnabled(False)   
        ui.btn_clearList.setEnabled(False)
        ui.btn_Print.setEnabled(False)

        ui.actionMove_Selected_Down_2.setEnabled(False)
        ui.actionMove_Selected_Up.setEnabled(False)
        ui.actionRemove_Selected_Item.setEnabled(False)
        ui.actionAdd_Item.setEnabled(False)
        ui.actionRemove_Selected_Item.setEnabled(False)
        ui.actionDisconnect_Selected.setEnabled(False)
        ui.actionClear_List.setEnabled(False)
        ui.actionPrint.setEnabled(False)
        ui.actionEdit_Item_Properties.setEnabled(False)
        ui.actionMove_Selected.setEnabled(False)

    else:
        ui.btn_MoveDown.setEnabled(True)
        ui.btn_MoveUp.setEnabled(True)
        ui.btn_Disconnect.setEnabled(True)
        ui.btn_addItem.setEnabled(True)   
        ui.btn_clearList.setEnabled(True)
        ui.btn_Print.setEnabled(True)

        ui.actionMove_Selected_Down_2.setEnabled(True)
        ui.actionMove_Selected_Up.setEnabled(True)
        ui.actionRemove_Selected_Item.setEnabled(True)
        ui.actionAdd_Item.setEnabled(True)
        ui.actionRemove_Selected_Item.setEnabled(True)
        ui.actionDisconnect_Selected.setEnabled(True)
        ui.actionClear_List.setEnabled(True)
        ui.actionPrint.setEnabled(True)
        ui.actionEdit_Item_Properties.setEnabled(True)
        ui.actionMove_Selected.setEnabled(True)
        
        

def FunctionGuiMap():

    #printer list: listPrinterList
    #queue list: list_PrintQueue

        
    '''GuiButtons'''
    #MainWindow
    ui.btn_MoveDown.clicked.connect(MoveDown)
    ui.btn_MoveUp.clicked.connect(MoveUp)
    ui.btn_Connect.clicked.connect(ConPrint)
    ui.btn_Disconnect.clicked.connect(test)
    ui.btn_addItem.clicked.connect(AddToQueue)   #important
    ui.btn_clearList.clicked.connect(test)
    ui.btn_Print.clicked.connect(test)

    QueueUI.btn_FileDialog.clicked.connect(FileDialogBox)
    QueueUI.checkBox.clicked.connect(test)
    QueueUI.PrintNumEdit.textChanged.connect(CheckItemNumberEntry)
    QueueUI.buttonBox.accepted.connect(VerifyAddItemEntry)

   

    ''' MenuBar'''
    #MainWindow
    ui.actionMove_Selected_Down_2.triggered.connect(MoveDown)
    ui.actionMove_Selected_Up.triggered.connect(MoveUp)
    ui.actionRemove_Selected_Item.triggered.connect(RemoveFromQueue)
    ui.actionExit.triggered.connect(EndProgram)
    ui.actionAdd_Item.triggered.connect(AddToQueue)    #important
    ui.actionRemove_Selected_Item.triggered.connect(test)
    ui.actionDisconnect_Selected.triggered.connect(test)
    ui.actionConnect.triggered.connect(ConPrint)
    ui.actionClear_List.triggered.connect(test)
    ui.actionPrint.triggered.connect(test)
    ui.actionEdit_Item_Properties.triggered.connect(test)
    ui.actionMove_Selected.triggered.connect(test)
    ui.actionPreferences.triggered.connect(test)
    ui.actionConfigure.triggered.connect(test)
    ui.actionAbout.triggered.connect(test)
    ui.actionDocumentation.triggered.connect(test)

    
    
def SetupDialogs():
    global QueueDialog
    global ConnectDialog
    global QueueUI
    global ConnectUI
    QueueDialog = queueDialog.QtGui.QDialog()
    QueueUI = queueDialog.Ui_Dialog()
    QueueUI.setupUi(QueueDialog)

    ConnectDialog = connectDialog.QtGui.QDialog()
    ConnectUI = connectDialog.Ui_Dialog()
    ConnectUI.setupUi(ConnectDialog)


#the main program
if __name__ == "__main__":
    app = gui.QtGui.QApplication(sys.argv)
    window = gui.QtGui.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(window)
    SetupDialogs()
    FunctionGuiMap()
    EnableButtons()
    window.show()
    sys.exit(app.exec_())


