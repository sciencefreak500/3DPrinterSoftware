#! /usr/bin/env python3
#pyusb and pyserial testing
import serial
import serial.tools.list_ports as listports

device = listports.comports()
for i in device:
        ID=str(i.vid+":"+i.pid)
        Port=str(i.device)






