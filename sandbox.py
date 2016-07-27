#! /usr/bin/env python3
#pyusb and pyserial testing

#import usb.core
import serial


#print(usb.core.find(idVendor=0x16c0,idProduct=0x0483))
ser=serial.Serial('/dev/ttyACM0',115200,timeout=1) #(port, baudrate, timeout
print(serial.Serial.get_settings(ser))
print(ser.readline())
ser.write(b''';FLAVOR:UltiGCode
;TIME:17726
;MATERIAL:32173
;MATERIAL2:0
;NOZZLE_DIAMETER:0.400000
;NOZZLE_DIAMETER2:0.400000

;Layer count: 408
;LAYER:0
M107
G0 F9000 X94.009 Y59.091 Z0.300
;TYPE:SKIRT
G1 X0 Y0 E0
G0 F9000 X0 Y0''')
print(ser.readline())
ser.close()
