#!/usr/bin/python
#This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, #You can obtain one at https://mozilla.org/MPL/2.0/
#Lookup table for 3D printer device ID's

def Printer():	#return command doesn't work unless in a function
	PrinterName=["Ultimaker2","Bukito","Red Wheel Mouse"] #Places in Arrays correspond with each other
	return PrinterName
def	Device(): 
	ID=["2341:0042","16c0:0483","04b3:310b"]
	return ID
Printer()
Device()
