#! /usr/bin/env python3
#This is a sandbox file

import serial
import serial.tools.list_ports as listports


arduino=['Arduino','9025:1']
device=listports.comports()
print(device)
for i in device:
	print(i)
	vid=str(i.vid)
	pid=str(i.pid)
	PortID= vid + ':' + pid
	print(PortID)
	if PortID == arduino[1]:
		Port= str(i.device)
		print('Arduino Found on Port '+Port)
		Found=True
	else:
		print('Arduino not Found')
if Found:
	ser = serial.Serial(Port,9600,timeout=5)
	print(serial.Serial.get_settings(ser))
	while True:
		choice=input('Read, Write, or Exit? (r,w,e)')
		if choice=='r':
			print(ser.readline())
		elif choice=='w':
			ser.write(b'sweep\n')
			print(ser.readline())
		else:
			break
