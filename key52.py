#!/usr/bin/env python

import sys
import evdev

devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]

if len(devices) == 0:
    print "No devices found, try running with sudo"
    sys.exit(1)

for device in devices:
    if device.name.strip(' ') == 'AB Shutter3':
        print(device)
        device.grab()
        sw = 0
        for event in device.read_loop():
            if event.type == evdev.ecodes.EV_KEY:
                #print(evdev.categorize(event))
                if   event.code==115 and event.value==1 and sw==0 : #A PRESS
                    print("A PRESS")
                elif event.code==115 and event.value==2 and sw==0 : #A HOLD
                    print("A HOLD")
                elif event.code==115 and event.value==0 and sw==0 : #A RERSE
                    print("A RERSE")
                elif event.code==115 and event.value==1 and sw==1 : #B PRESS
                    print("B PRESS")
                elif event.code==115 and event.value==2 and sw==1 : #B HOLD
                    print("B HOLD")
                elif event.code==115 and event.value==0 and sw==1 : #B RERSE
                    print("B RERSE")
                elif event.code==28  and event.value==1 : #B ENTER PRESS
                    print("B ENTER PRESS")
                    sw = 1
                elif event.code==28  and event.value==2 : #B ENTER HOLD A=>B
                    print("B ENTER HOLD")
                elif event.code==28  and event.value==0 : #B ENTER RERSE
                    print("B ENTER RERSE")
                    sw = 0
                else: # OTHER
                    print("OTHER")
                    print(evdev.categorize(event))

#KEY_VOLUMEUP 115
#KEY_ENTER 28
#down hold up
