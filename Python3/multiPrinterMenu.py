#! /usr/bin/env python3
#This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, #You can obtain one at https://mozilla.org/MPL/2.0/
#Second TK user menu, in order to pick which printer or printers to connect to in case of multiple printers

import tkinter
from tkinter import messagebox

def Main():
	class MyGUI:
		def __init__(self):
		# Create the main window.
			self.main_window = tkinter.Tk()

		# Create two frames. One for the checkbuttons
		# and another for the regular Button widgets.
			self.top_frame = tkinter.Frame(self.main_window)
			self.bottom_frame = tkinter.Frame(self.main_window)

			self.label=tkinter.Label(self.top_frame,text="Choose as many printers you want to connect to.")
			self.label.pack()
		# Create three IntVar objects to use with
		# the Checkbuttons.
			self.cb_var1 = tkinter.IntVar()
			self.cb_var2 = tkinter.IntVar()
			self.cb_var3 = tkinter.IntVar()

		# Set the intVar objects to 0.
			self.cb_var1.set(0)
			self.cb_var2.set(0)
			self.cb_var3.set(0)
		# Create the Checkbutton widgets in the top_frame.
			self.cb1 = tkinter.Checkbutton(self.top_frame, \
text='Option 1', variable=self.cb_var1)
			self.cb2 = tkinter.Checkbutton(self.top_frame, \
text='Option 2', variable=self.cb_var2)
			self.cb3 = tkinter.Checkbutton(self.top_frame, \
text='Option 3', variable=self.cb_var3)

		# Pack the Checkbuttons.
			self.cb1.pack()
			self.cb2.pack()
			self.cb3.pack()
			

		# Create an OK button and a Quit button.
			self.connect_button = tkinter.Button(self.bottom_frame, \
  text='Connect', command=self.show_choice)
			self.notFound_button = tkinter.Button(self.bottom_frame, \
  text='Printer not Displayed', command=print("Secondary connection functionality")

		# Pack the Buttons.
			self.connect_button.pack(side='left')
			self.notFound_button.pack(side='left')

		# Pack the frames.
			self.top_frame.pack()
			self.bottom_frame.pack()

		# Start the mainloop.
			tkinter.mainloop()
		# The show_choice method is the callback function for the OK button.

		def show_choice(self):
			global Printers
			Printers=[]
		# Determine which Checkbuttons are selected 
			Printers.append(str(self.cb_var1.get()))
			return Printers
	# Create an instance of the MyGUI class.
	my_gui = MyGUI()
