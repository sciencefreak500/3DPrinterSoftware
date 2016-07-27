#! /usr/bin/env python3
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
			self.cb_var0 = IntVar()
			self.cb_var0.set(0)
			self.cb0 = Checkbutton(self.middle_frame, text='Bukito', variable=self.cb_var0,command=self.fcb0)
			self.cb0.pack()
			self.add_button = Button(self.bottom_frame,text='Add to Queue',command=self.show_choice)
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
		# The show_choice method is the callback function for the add to queue button.
		def fcb0(self):
			if self.cb_var0.get()==0:
				self.cb_var0.set(1)
			else:
				self.cb_var0.set(0)
		def show_choice(self):
			printers=[]
			if str(self.cb_var0.get())=='1':
				printers.append('Bukito')
			number=int(self.number_entry.get())
			QueueAddition = {'Name': fileName, 'Path': filepath, 'Printers': printers, 'Number': number}
			with open('setup.inf','wb') as f:
				pickle.dump([QueueAddition], f)
			self.main_window.quit()
			self.main_window.destroy()
	# Create an instance of the MyGUI class.
	my_gui = MyGUI()