#! /usr/bin/env python3
#This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, #You can obtain one at https://mozilla.org/MPL/2.0/
#Second TK user menu, in order to pick which printer or printers to connect to in case of multiple printers

import tkinter
import pickle

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
		# Create IntVar objects to use with
		# the Checkbuttons.
			self.cb_var0 = tkinter.IntVar()
			self.cb_var0.set(0)
			self.cb0 = tkinter.Checkbutton(self.top_frame, text='Red Wheel Mouse', variable=self.cb_var0,command=self.fcb0)
			self.cb0.pack()
			self.cb_var1 = tkinter.IntVar()
			self.cb_var1.set(0)
			self.cb1 = tkinter.Checkbutton(self.top_frame, text='Bukito', variable=self.cb_var1,command=self.fcb1)
			self.cb1.pack()
			self.connect_button = tkinter.Button(self.bottom_frame,text='Connect',command=self.show_choice)
			self.notFound_button = tkinter.Button(self.bottom_frame, text='Printer not Displayed')
			self.notFound_button["command"] = self.secConFunct
		# Pack the Buttons.
			self.connect_button.pack(side='left')
			self.notFound_button.pack(side='left')


		# Pack the frames.
			self.top_frame.pack()
			self.bottom_frame.pack()

		# Start the mainloop.
			tkinter.mainloop()
		def secConFunct(self):
			print("Secondary connection functionality")
		# The show_choice method is the callback function for the connect button.
		def fcb0(self):
			if self.cb_var0.get()==0:
				self.cb_var0.set(1)
			else:
				self.cb_var0.set(0)
		def fcb1(self):
			if self.cb_var1.get()==0:
				self.cb_var1.set(1)
			else:
				self.cb_var1.set(0)
		def show_choice(self):
			Printers=[]
			Printers.append(str(self.cb_var0.get()))
			Printers.append(str(self.cb_var1.get()))
			with open('setup.inf','wb') as f:
				pickle.dump([Printers], f)
			self.main_window.quit()
			self.main_window.destroy()
	# Create an instance of the MyGUI class.
	my_gui = MyGUI()