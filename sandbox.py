#! /usr/bin/env python3
#Second TK user menu, in order to pick which printer or printers to connect to in case of multiple printers

import tkinter
from tkinter import messagebox

def Main():
	class MyGUI:
		def __init__(self):
		#mpk Create the main window.
			self.main_window = tkinter.Tk()

		#mpk Create two frames. One for the checkbuttons
		#mpk and another for the regular Button widgets.
			self.top_frame = tkinter.Frame(self.main_window)
			self.bottom_frame = tkinter.Frame(self.main_window)

		#mpk Create three IntVar objects to use with
		#mpk the Checkbuttons.
			self.cb_var1 = tkinter.IntVar()
			self.cb_var2 = tkinter.IntVar()
			self.cb_var3 = tkinter.IntVar()

		#mpk Set the intVar objects to 0.
			self.cb_var1.set(0)
			self.cb_var2.set(0)
			self.cb_var3.set(0)
		#mpk Create the Checkbutton widgets in the top_frame.
			self.cb1 = tkinter.Checkbutton(self.top_frame, \
text='Option 1', variable=self.cb_var1)
			self.cb2 = tkinter.Checkbutton(self.top_frame, \
text='Option 2', variable=self.cb_var2)
			self.cb3 = tkinter.Checkbutton(self.top_frame, \
text='Option 3', variable=self.cb_var3)

		#mpk Pack the Checkbuttons.
			self.cb1.pack()
			self.cb2.pack()
			self.cb3.pack()

		#mpk Create an OK button and a Quit button.
			self.ok_button = tkinter.Button(self.bottom_frame, \
  text='Connect', command=self.show_choice)
			self.quit_button = tkinter.Button(self.bottom_frame, \
  text='Printer not Displayed', command=self.main_window.quit)

		#mpk Pack the Buttons.
			self.ok_button.pack(side='left')
			self.quit_button.pack(side='left')

		#mpk Pack the frames.
			self.top_frame.pack()
			self.bottom_frame.pack()

		#mpk Start the mainloop.
			tkinter.mainloop()
		#mpk The show_choice method is the callback function for the OK button.

		def show_choice(self):
		#mpk Create a message string.
			self.message = 'You selected:\n'

		#mpk Determine which Checkbuttons are selected and build the message string accordingly.
			if self.cb_var1.get() == 1:
				self.message = self.message + '1\n'
			if self.cb_var2.get() == 1:
				self.message = self.message + '2\n'
			if self.cb_var3.get() == 1:
				self.message = self.message + '3\n'

		#mpk Display the message in an info dialog box.
			messagebox.showinfo('Selection', self.message)

	#mpk Create an instance of the MyGUI class.
	my_gui = MyGUI()
Main()
