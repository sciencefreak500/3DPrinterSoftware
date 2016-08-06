#! /usr/bin/env python3
#pyusb and pyserial testing

#import usb.core
import serial


#print(usb.core.find(idVendor=0x16c0,idProduct=0x0483))
ser=serial.Serial('/dev/ttyACM0',115200,timeout=1) #(port, baudrate, timeout
print(serial.Serial.get_settings(ser))
print(ser.readline())
ser.write(b'''G92 E0
G28
''')
print(ser.readline())
ser.close()
