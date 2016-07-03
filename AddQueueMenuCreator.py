#! /usr/bin/env python3
#This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, #You can obtain one at https://mozilla.org/MPL/2.0/

import AddQueueMenu
import pickle
import importlib      

def Main():
	with open('setup.inf','rb') as f:
		conPrinters=pickle.load(f)
	conPrinters=conPrinters[0]
	with open("AddQueueMenu.py",'w') as f:
		f.write("""#! /usr/bin/env python3
#This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, #You can obtain one at https://mozilla.org/MPL/2.0/
#Popup TK user menu, in order to add files to queue

from tkinter import filedialog
from tkinter import *
import pickle

def Main():
	class MyGUI:
		def __init__(self):
		# Create the main window.
			self.main_window = Tk()

		# Create two frames. One for the checkbuttons
		# and another for the regular Button widgets.
			self.top_frame = Frame(self.main_window)
			self.middle_frame = Frame(self.main_window)
			self.bottom_frame = Frame(self.main_window)
			self.prompt_label = Label(self.top_frame, text='Enter number of times to print file:')
			self.number_entry = Entry(self.top_frame, width=10)
#mpk Pack the top frame's widgets.
			self.prompt_label.pack(side='left')
			self.number_entry.pack(side='left')

			self.file_button = Button(self.middle_frame,text='Choose File',command=self.filedialog)
			
			self.chooseFileLabel=StringVar()
			self.choosefilelabel=Label(self.middle_frame,textvariable=self.chooseFileLabel)

			self.label=Label(self.middle_frame,text="Choose which printers to send this file too.")
			self.file_button.pack()
			self.choosefilelabel.pack()
			self.label.pack()
		# Create IntVar objects to use with
		# the Checkbuttons.
""")
		n=0
		while n<len(conPrinters) and str(conPrinters[0])!="[]":
			Name=str(conPrinters[n])
			f.write("			self.cb_var"+str(n)+" = IntVar()\n")
			f.write("			self.cb_var"+str(n)+".set(0)\n")
			f.write("			self.cb"+str(n)+" = Checkbutton(self.middle_frame, \
text='"+Name+"', variable=self.cb_var"+str(n)+",command=self.fcb"+str(n)+")\n")
			f.write("			self.cb"+str(n)+".pack()\n")
			n+=1
		f.write("""			self.add_button = Button(self.bottom_frame,text='Add to Queue',command=self.show_choice)
			self.notFound_button = Button(self.bottom_frame, text='Printer not Displayed')
			self.notFound_button["command"] = self.secConFunct
		# Pack the Buttons.
			self.add_button.pack(side='left')
			self.notFound_button.pack(side='left')


		# Pack the frames.
			self.top_frame.pack()
			self.middle_frame.pack()
			self.bottom_frame.pack()

		# Start the mainloop.
			mainloop()
		def secConFunct(self):
			print("Printer Connect functionality")
		def filedialog(self):
			global filepath
			global fileName
			filepath=filedialog.askopenfilename()
			fileName = filepath.split('/')[-1]
			self.chooseFileLabel.set("File Selected:"+str(fileName))
		# The show_choice method is the callback function for the add to queue button.\n""")
		n=0
		while n<len(conPrinters) and str(conPrinters[0])!="[]":
			f.write("		def fcb"+str(n)+"(self):\n")
			f.write("			if self.cb_var"+str(n)+".get()==0:\n")
			f.write("				self.cb_var"+str(n)+".set(1)\n")
			f.write("			else:\n")
			f.write("				self.cb_var"+str(n)+".set(0)\n")
			n+=1
		f.write("""		def show_choice(self):
			printers=[]\n""")
		n=0
		while n<len(conPrinters) and str(conPrinters[0])!="[]":
			Name=str(conPrinters[n])
			f.write("			if str(self.cb_var"+str(n)+".get())=='1':\n")
			f.write("				printers.append('"+str(Name)+"')\n")
			n+=1
		f.write("""			number=int(self.number_entry.get())
			QueueAddition = {'Name': fileName, 'Path': filepath, 'Printers': printers, 'Number': number}
			with open('setup.inf','wb') as f:
				pickle.dump([QueueAddition], f)
			self.main_window.quit()
			self.main_window.destroy()
	# Create an instance of the MyGUI class.
	my_gui = MyGUI()""")
	importlib.reload(AddQueueMenu)
	AddQueueMenu.Main()
