#!/usr/bin/env python
import sys

if sys.platform == 'win32':
	import os
	import win32com.shell.shell as shell
	ASADMIN = 'asadmin'

	if sys.argv[-1] != ASADMIN:
		script = os.path.abspath(sys.argv[0])
		params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
		shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    

#below checks for different versions of compiler for python
#loads different dll's for libusb

f = open('C:\Windows\System32\SeriouslyFakeTest.dll','w')
f.close()

check = sys.version

if 'MSC' in check:
    if 'AMD' in check:
        if '32' in check:
            print("32 bit MSC AMD")
        elif '64' in check:
            print("64 bit MSC AMD")
    elif 'Intel' in check:
        if '32' in check:
            print("32 bit MSC Intel")
        elif '64' in check:
            print("64 bit MSC Intel")
elif 'GCC' in check:
	if '2' in check.split(' ')[0].split('.')[0]:
		print("version 2 GCC")
	elif '3' in check.split(' ')[0].split('.')[0]:
		print("version 3 GCC")

		