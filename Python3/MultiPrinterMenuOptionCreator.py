#! /usr/bin/env python3
#This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, #You can obtain one at https://mozilla.org/MPL/2.0/

import MultiPrinterMenu
import pickle
import importlib

def Main():
	with open('setup.inf','rb') as f:
		Names=pickle.load(f)
	with open("MultiPrinterMenu.py",'w') as f:
		f.write("""#! /usr/bin/env python3
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
""")
		n=0
		while n<len(Names) and str(Names[0])!="[]":
			Name=str(Names[n])
			f.write("			self.cb_var"+str(n)+" = tkinter.IntVar()\n")
			f.write("			self.cb_var"+str(n)+".set(0)\n")
			f.write("			self.cb"+str(n)+" = tkinter.Checkbutton(self.top_frame, \
text='"+Name[2:len(Name)-2]+"', variable=self.cb_var"+str(n)+",command=self.fcb"+str(n)+")\n")
			f.write("			self.cb"+str(n)+".pack()\n")
			n+=1
		f.write("""			self.connect_button = tkinter.Button(self.bottom_frame,text='Connect',command=self.show_choice)
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
		# The show_choice method is the callback function for the connect button.\n""")
		n=0
		while n<len(Names) and str(Names[0])!="[]":
			f.write("		def fcb"+str(n)+"(self):\n")
			f.write("			if self.cb_var"+str(n)+".get()==0:\n")
			f.write("				self.cb_var"+str(n)+".set(1)\n")
			f.write("			else:\n")
			f.write("				self.cb_var"+str(n)+".set(0)\n")
			n+=1
		f.write("""		def show_choice(self):
			Printers=[]\n""")
		n=0
		while n<len(Names) and str(Names[0])!="[]":
			f.write("			Printers.append(str(self.cb_var"+str(n)+".get()))\n")
			n+=1
		f.write("""			with open('setup.inf','wb') as f:
				pickle.dump([Printers], f)
			self.main_window.quit()
			self.main_window.destroy()
	# Create an instance of the MyGUI class.
	my_gui = MyGUI()""")
	importlib.reload(MultiPrinterMenu)
	MultiPrinterMenu.Main()
