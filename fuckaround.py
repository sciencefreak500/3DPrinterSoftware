#! /usr/bin/env python
#adding menu pop up for printer connect and adding files to queue

from Tkinter import *

master = Tk()

var = StringVar(master)
var.set("Bukito") # initial value

option = OptionMenu(master, var, "Bukito", "Ultimaker2", "Red Wheel Mouse","other")
option.pack()
#set1.diffrence(set2) #start of in case printer doesn't appear in list function
#
# test stuff

def ok():
    print "value is", var.get()
    master.quit()

button = Button(master, text="OK", command=ok)
button.pack()

master.mainloop()
